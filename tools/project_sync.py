"""Put every open issue of every public Unseenet repository on the organisation's
project board (https://github.com/orgs/unseenet/projects/1), with Status
"Todo" and a Kind from its labels, when it is not there yet. Run by
.github/workflows/project-sync.yml with GH_TOKEN = the PROJECT_TOKEN secret
(fine-grained, owner unseenet: Issues read, Projects read and write)."""
import json, subprocess, sys

OWNER, NUMBER = "unseenet", "1"


def gh(*a):
    r = subprocess.run(["gh", *a], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"gh {' '.join(a[:3])}: {r.stderr.strip()}")
    return json.loads(r.stdout) if r.stdout.strip() else None


def kind_of(issue):
    labels = {l["name"] for l in issue["labels"]}
    if "bug" in labels:
        return "Bug"
    if "area: protocol" in labels or issue["title"].startswith("UN-RFC"):
        return "Protocol"
    if "area: infra" in labels or issue["title"].startswith(("CI:", "Docker:", "Repos:")):
        return "Infra"
    return "Feature"


def main():
    project = next(p for p in gh("project", "list", "--owner", OWNER, "--format", "json")["projects"]
                   if str(p["number"]) == NUMBER)
    fields = {f["name"]: f for f in gh("project", "field-list", NUMBER, "--owner", OWNER, "--format", "json")["fields"]}
    option = lambda field, name: next(o["id"] for o in fields[field]["options"] if o["name"] == name)
    have = {i["content"].get("url") for i in gh("project", "item-list", NUMBER, "--owner", OWNER, "--limit", "2000",
                                                 "--format", "json")["items"] if i.get("content")}
    repos = [r["name"] for r in gh("repo", "list", OWNER, "--limit", "100", "--json", "name,isArchived,visibility")
             if not r["isArchived"] and r["visibility"] == "PUBLIC" and not r["name"].startswith(".")]
    added = 0
    for repo in sorted(repos):
        for issue in gh("issue", "list", "-R", f"{OWNER}/{repo}", "--state", "open", "--limit", "500",
                        "--json", "url,labels,title"):
            if issue["url"] in have:
                continue
            item = gh("project", "item-add", NUMBER, "--owner", OWNER, "--url", issue["url"], "--format", "json")
            for field, value in (("Status", "Todo"), ("Kind", kind_of(issue))):
                gh("project", "item-edit", "--id", item["id"], "--project-id", project["id"],
                   "--field-id", fields[field]["id"], "--single-select-option-id", option(field, value))
            print(f"added {issue['url']} ({kind_of(issue)})")
            added += 1
    print(f"{added} added, {len(have)} were there already")


if __name__ == "__main__":
    main()
