# How the Unseenet repositories work

Decided in [unseenet#391](https://github.com/unseenet/unseenet/issues/391);
the shared workflows are in this repository (unseenet#545).

## Layout

| | |
|---|---|
| `src/<package>/` | the code, a Python package |
| `tests/` | pytest |
| `docs/` + `mkdocs.yml` | the docs of what this repository holds, previewable alone (`mkdocs serve`); [unseenet-docs](https://github.com/unseenet/unseenet-docs) gathers them into unseenet.org |
| `CHANGELOG.md` | [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with `## [Unreleased]` on top |
| `README.md` | what the repository holds, and the section *Part of Unseenet* listing every repository |

Build repositories (`unseenet-portable`, `unseenet-bootable`) hold no client
code: a `versions.toml` naming what to take, the build tools and the
workflows.

## Issues and milestones

- **An issue lives where the change is made**: the protocol (UN-RFCs), the
  core, the node and the CLI in `unseenet`; a client, a build, a service or
  the site in its own repository. Something wrong or missing in the graphical
  client is an issue in unseenet-gui, not in unseenet.
- **Milestones follow each repository's own versions.** unseenet's next is
  its next core version (0.6.0); unseenet-gui's is the next GUI version
  (0.3.0), and so on - plus `Later`. The build repositories (portable,
  bootable) are versioned as the core they carry, so their milestones are
  named like the core's. unseenet-docs has no releases and no milestones.
- **A core change others must follow** gets its issue in `unseenet`, and an
  issue in every repository that must follow it, linked both ways ("needs
  unseenet 0.6" in the follow-up; the list of follow-ups in the core issue).
  The follow-up goes in that repository's own next milestone.
- **Work across several repositories** gets one tracking issue in
  `unseenet` that links an issue in each.
- **One board for everything**: the organisation's project
  [Unseenet](https://github.com/orgs/unseenet/projects/1) holds every open
  issue of every repository (new ones are added by themselves), with its
  repository, milestone, status and kind (Bug, Feature, Protocol, Infra).
- **Every core minor release has a release plan**: one issue in `unseenet`
  ("0.6.0 release plan") that lists the core milestone and every follow-up in
  the other repositories that must be done for it, and the order: core,
  nodes, clients and services, the bundle (portable, bootable), signing.

## Versions

- Each repository numbers its own releases with semantic versioning on the
  core's principles. A client or service may release while the core stays on
  one version; which core it needs is in `pyproject.toml`
  (`unseenet>=0.5,<0.6`, one minor version at a time) and at the top of its
  release notes.
- Bundles (portable zips, bootable images) are versioned as the core they
  carry: `0.6.0`. A rebuild with newer clients is `0.6.0.post1`.
- Tags `vX.Y.Z` on `main`. A `release/X.Y` branch is made only when a fix
  for that series is needed. Pre-alpha: no compatibility code for older
  nodes - update the nodes first.

## Workflows

Nothing is built on merge: pull requests and `main` run the tests.

| Workflow here | Use |
|---|---|
| `python-tests.yml` | tests on pull requests and `main`; `core-main: true` in clients and services |
| `docs-check.yml` | `mkdocs build --strict` of `docs/` on pull requests |
| `release-build.yml` + `release-github.yml` | a release on a `v*` tag: version and changelog checked, tests, package, GitHub release with the changelog section; the PyPI step stays in the repository (trusted publishing does not accept reusable workflows) |
| `nightly-gate.yml` | build repositories: build each night only when something changed since the `dev` pre-release |

A short workflow in a repository:

```yaml
name: tests
on:
  push: {branches: [main]}
  pull_request:
jobs:
  tests:
    uses: unseenet/.github/.github/workflows/python-tests.yml@main
    with: {core-main: true}
  docs:
    if: github.event_name == 'pull_request'
    uses: unseenet/.github/.github/workflows/docs-check.yml@main
```

## Builds

Portable and bootable builds run **nightly** (only when something changed),
**by hand** (`publish`: `dev` or `artifact`; `force`) and on **release tags**.
The `dev` pre-release is the newest nightly build; sticks on the development
channel take it, signed with the CI release key. Stable releases are signed
by the maintainer with the project key.
