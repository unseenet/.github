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
