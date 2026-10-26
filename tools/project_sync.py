"""Put every open issue and pull request of every public Unseenet repository on
the organisation's project board (https://github.com/orgs/unseenet/projects/1),
with Status "Todo" and a Kind from its labels, when it is not there yet.

Every item also gets "From": "Core" when it was opened by the core team (CORE
below, the organisation's public members, or a bot), otherwise "Community" -
so a project view filtered on from:Community shows what others bring in.
"From" is filled in on items already on the board too, but never overwritten.

Run by .github/workflows/project-sync.yml with GH_TOKEN = the PROJECT_TOKEN
secret (fine-grained, owner unseenet: Issues read, Pull requests read,
Projects read and write)."""
import json, subprocess, sys

OWNER, NUMBER = "unseenet", "1"
CORE = {"andlo"}  # core team; public org members are added automatically


def gh(*a):
    r = subprocess.run(["gh", *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"gh {' '.join(a[:3])}: {r.stderr.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def kind_of(item):
    labels = {l["name"] for l in item["labels"]}
    if "bug" in labels:
        return "Bug"
    if "area: protocol" in labels or item["title"].startswith("UN-RFC"):
        return "Protocol"
    if "area: infra" in labels or item["title"].startswith(("CI:", "Docker:", "Repos:")):
        return "Infra"
    return "Feature"


def main():
    project = next(p for p in gh("project", "list", "--owner", OWNER, "--format", "json")["projects"]
                   if str(p["number"]) == NUMBER)
    fields = {f["name"]: f for f in gh("project", "field-list", NUMBER, "--owner", OWNER, "--format", "json")["fields"]}
    option = lambda field, name: next(o["id"] for o in fields[field]["options"] if o["name"] == name)

    def set_field(item_id, field, value):
        gh("project", "item-edit", "--id", item_id, "--project-id", project["id"],
           "--field-id", fields[field]["id"], "--single-select-option-id", option(field, value))

    core = CORE | {m["login"] for m in gh("api", f"orgs/{OWNER}/public_members")}
    from_of = lambda item: "Core" if item["author"].get("is_bot") or item["author"]["login"] in core else "Community"

    # url -> (project item id, current "From" value or None)
    have = {i["content"]["url"]: (i["id"], i.get("from"))
            for i in gh("project", "item-list", NUMBER, "--owner", OWNER, "--limit", "2000", "--format", "json")["items"]
            if i.get("content", {}).get("url")}
    repos = [r["name"] for r in gh("repo", "list", OWNER, "--limit", "100", "--json", "name,isArchived,visibility")
             if not r["isArchived"] and r["visibility"] == "PUBLIC" and not r["name"].startswith(".")]
    added = tagged = 0
    for repo in sorted(repos):
        for cmd in ("issue", "pr"):
            for item in gh(cmd, "list", "-R", f"{OWNER}/{repo}", "--state", "open", "--limit", "500",
                           "--json", "url,labels,title,author"):
                origin = from_of(item)
                if item["url"] in have:
                    item_id, current = have[item["url"]]
                    if not current:
                        set_field(item_id, "From", origin)
                        tagged += 1
                    continue
                new = gh("project", "item-add", NUMBER, "--owner", OWNER, "--url", item["url"], "--format", "json")
                for field, value in (("Status", "Todo"), ("Kind", kind_of(item)), ("From", origin)):
                    set_field(new["id"], field, value)
                print(f"added {item['url']} ({kind_of(item)}, {origin})")
                added += 1
    print(f"{added} added, {tagged} tagged with From, {len(have)} were there already")


if __name__ == "__main__":
    main()
