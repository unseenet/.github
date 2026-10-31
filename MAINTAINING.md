# Becoming a maintainer: a step-by-step guide

This guide explains how someone becomes a maintainer of the unseenet GitHub
organisation, and what they have to do. The rules themselves are in
[GOVERNANCE.md](GOVERNANCE.md); this is how to follow them.

**You don't need any of this to contribute.** Anybody can open issues and
pull requests, and there is nothing to sign.

## What being a maintainer means

- **You may** merge pull requests, create tags and run the release
  workflows in the repositories you are given.
- **You commit to** following the UN-RFCs, saying what is built,
  respecting the network's decisions, putting no hidden powers in the code,
  signing and keeping releases, and working in the open (GOVERNANCE.md,
  *Commitments*).
- **You don't have to** give your real name. Any GitHub account will do.

## The steps

### 1. Contribute for a while

There is no fixed number of contributions. A maintainer has to have seen
enough of your work to trust it.

### 2. Be proposed

A maintainer opens an issue in
[unseenet/.github](https://github.com/unseenet/.github/issues), titled
`Maintainer: <your GitHub login>`, saying which repositories you would
maintain and why. If no maintainer objects within 14 days, you may go on.

### 3. Get your account ready

- **Turn on two-factor authentication** on your GitHub account
  (*Settings → Password and authentication*).
- **Keep your recovery codes** somewhere offline.

### 4. Read GOVERNANCE.md and note its version

Read [GOVERNANCE.md](GOVERNANCE.md) as it is on `main`. Then find the commit
of the version you read, either under *History* on GitHub, or locally:

```
git log -1 --format=%h -- GOVERNANCE.md
```

### 5. Open your pledge pull request

From **your own account**:

1. Fork unseenet/.github, or make a branch if you already have access.
2. Add a row to [MAINTAINERS.md](MAINTAINERS.md):

   ```
   | <your login> | maintainer | I have read GOVERNANCE.md at commit `<hash>` and commit to it. | <your Unseenet key, or -> |
   ```

3. Open a pull request titled `MAINTAINERS.md: <your login>'s pledge`.

The pull request is your signature. It stays in the history, and the hash
shows which version you agreed to.

### 6. Optional: make the pledge in the network too

If you want people in Unseenet to be able to recognise you, post the same
statement with your Unseenet identity. It is signed with your key
automatically:

```
unseenet post unseenet.help@ph5fc5hop5232qsz \
  --subject "Maintainer pledge: <your login>" \
  --body "I am <your login> on GitHub. I have read GOVERNANCE.md at commit <hash> and commit to it."
```

Then put the key that `unseenet whoami` shows in the last column of your row
in MAINTAINERS.md. Your GitHub account and your key now point to each other.

Use the council's talk group (UN-RFC 0061) instead, once it exists.

**Think before you link.** Linking a key to your GitHub account means that
whatever you have posted with that key can be tied to that account. If you
want your everyday identity to stay unlinked, make a separate identity for
this (`unseenet id-new`) and pledge with that one. You can also skip this
step entirely: the pull request is enough.

### 7. An owner lets you in

An owner checks the following, merges your pull request, and gives you
access:

- the pull request came from the same account that was proposed;
- 14 days have passed without an objection;
- two-factor authentication is on.

## Later

- **When GOVERNANCE.md changes in substance**, every maintainer confirms the
  new version: a pull request that updates the hash in their row.
- **Stepping down**: a pull request that removes your row. Your access is
  then taken away. You can come back the same way you came in.
- **Inactive for 12 months**: your access is taken away and your row is
  marked inactive. You get it back by asking.
- **Breaking a commitment**: an owner removes your access and explains why
  in a public issue (GOVERNANCE.md, *Roles*).

## Becoming an owner

The same steps, with `owner` as the role, given by the existing owners. The
organisation should have at least two owners.
