# Governance of the unseenet GitHub organisation

**Draft for review.** Nothing here is in force before it is merged.

## What this GitHub organisation is

This GitHub organisation (github.com/unseenet) is **one project**: it writes one implementation of
Unseenet and is one publisher of releases (UN-RFC 0062). It does not own the
protocol or the network.

- **The protocol** is the UN-RFC series (UN-RFC 0000). Once UN-RFC 0063 is
  built, it lives in the network and changes by a council's public hearing.
- **The network's lists, its registrar and its own hierarchy** are kept by
  councils (UN-RFC 0020, 0054, 0055).
- **Anyone may build nodes, clients and releases** that follow the UN-RFCs.
  Theirs are as valid as ours.

What follows binds everyone with write access to a repository of this
GitHub organisation.

## Commitments

1. **Follow the UN-RFCs.** Anything that goes over the network is written
   in a UN-RFC first, as a Draft or Experimental, never only in code. When
   code and a UN-RFC disagree, one of them is fixed in the open. Something
   the reference code does that the UN-RFCs do not say is a fault in the
   UN-RFCs, and is reported as one (UN-RFC 0062 section 7).
2. **Say what is built.** Every Standards Track header's `Implemented:`
   line states what runs and what is missing (UN-RFC 0000 section 3.4).
3. **Respect the network's decisions.**
   - A proposal that passed its hearing (UN-RFC 0061) is binding for what the
     project's code aims at.
   - Once the series is in the network (UN-RFC 0063), `rfc/` changes only
     through its mirror.
   - Once a council keeps the lists (UN-RFC 0020), the lists change only by
     its rules, never by a pull request.
4. **No hidden powers.** Nothing in the project's code may give the project,
   its keys or anybody else a power the UN-RFCs do not give. That rules out
   backdoors, telemetry, kill switches and keys that bypass a council.
5. **Releases are signed and kept.**
   - Every release is signed as UN-RFC 0062 says. Once the project's key
     list has threshold 2, no single person can publish alone.
   - Every release carries its source bundle (UN-RFC 0062 section 5), which
     scribes keep (UN-RFC 0020 section 6.4).
6. **Work in the open.** Decisions are made in issues and pull requests.
   Once the network carries them, they are made in the network's own groups.

## Roles

| Role | Can | How you get it | How you lose it |
|---|---|---|---|
| Owner | everything, including the organisation's settings | by the owners | by stepping down, or by the other owners for breaking a commitment |
| Maintainer | merge, tag, run release workflows | proposed by a maintainer, after sustained contributions; given when no maintainer objects within 14 days | inactive for 12 months (given back on asking), or for breaking a commitment |
| Contributor | issues and pull requests | anybody | - |

- **Any name is accepted.** Nobody has to say who they are to hold a role.
  A maintainer MAY link their Unseenet identity key to their account, so
  that people in the network can recognise them.
- **Removing a role for breaking a commitment** is stated in a public issue,
  with the reason.
- **At least two owners**, so that the project does not stop when one
  person does.

## The maintainer's pledge

Before someone becomes a maintainer or an owner, they open a pull request
that adds them to [MAINTAINERS.md](MAINTAINERS.md) with the line

> I have read GOVERNANCE.md at commit `<hash>` and commit to it.

The pull request from their own account is the signature, and it stays in
the history. The hash says which version they agreed to. They MAY also post
the same statement in the network, signed with their Unseenet identity key,
so that people there can see who can change the code. When this document
changes in substance, maintainers confirm the new version the same way.

**Contributors sign nothing.** A pull request is given under the
repository's own licence. There is no CLA, no sign-off line and no
requirement to sign commits. Taking part has to stay as easy as opening a
pull request.

## If the GitHub organisation disappears

The network does not need it. Other publishers can release (UN-RFC 0062),
scribes keep the code (UN-RFC 0020 section 6.4), and councils keep the lists
and the series. The licences let anyone fork everything. This document is a
promise; the guarantee is that nothing depends on it.

## Enforcement on GitHub (proposed, not yet switched on)

Rulesets on every repository's default branch:

- **Main:** changes only by pull request, never force-pushed or deleted.
- **Required checks:** each repository's tests; in `unseenet` also
  `tools/check_rfc_headers.py`.
- **No required approvals.** While there may be only one maintainer, a
  required review would stop all work. Checks, not people, guard main.
- **Squash merge.** GitHub signs the merge commit, so main is signed
  without contributors having to sign anything.
- **Release tags** (`v*`, `unseenet-gui *`, …) are created only by the
  release workflows.
- **`rfc/`:** once the mirror runs, only the mirror changes it (CODEOWNERS).
- **Bypass:** owners may bypass in an emergency. GitHub logs each bypass,
  and the owner explains it in an issue.

These change how the maintainers themselves push, so they are switched on
only after this document is merged.

## Where things stand (informative)

Today the GitHub organisation has one owner and one maintainer: the founder. Just
as the councils are in their founding period (UN-RFC 0054 section 19), the
roles above are written for people who have not joined yet.

## Changing this document

By pull request. It stays open for at least 14 days, is announced in
`unseenet.announce`, and is merged only when no maintainer objects.
