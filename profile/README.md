<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-dark.svg">
    <img src="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-light.svg" alt="Unseenet" width="360">
  </picture>
</p>

<p align="center"><b>Usenet, unseen.</b><br>
A decentralized, encrypted discussion network in the spirit of Usenet and the BBSes - over Tor.</p>

<p align="center">
  <a href="https://unseenet.org"><b>unseenet.org</b></a> ·
  <a href="https://unseenet.org/guide/">How it works</a> ·
  <a href="https://unseenet.org/guide/threats/">The threat model</a> ·
  <a href="https://unseenet.org/spec/">The UN-RFCs</a> ·
  <a href="https://stats.unseenet.org/">Network statistics</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/overview.svg" alt="Clients reach nodes over Tor; nodes are onion services peering with each other; a web entrance lets a browser in, a gateway links other networks" width="760">
</p>

Groups and chats live on nodes anyone can run, linked over Tor onion
services. Nobody owns the network: no company decides who may post, nobody
can remove a group or sort what you see, and nobody can profile you. Posts
are signed, closed groups and private posts are end-to-end encrypted, and the
protocol is written down as numbered RFC-style documents, so anyone can build
a node or a client - like in the old days.

> **Pre-alpha.** Nothing is stable yet, and nothing has had a security review.
> Play with it, pick it apart - do not rely on it to protect anyone yet.

### Start here

| I want to… | |
|---|---|
| **use it** | the [graphical](https://github.com/unseenet/unseenet-gui) or [terminal](https://github.com/unseenet/unseenet-tui) client - [portable](https://github.com/unseenet/unseenet-portable) on a stick, [bootable](https://github.com/unseenet/unseenet-bootable), or in a browser through a [web entrance](https://github.com/unseenet/unseenet-entrance) |
| **run a node** | one command on Debian or Ubuntu, or Docker: [Running a node](https://unseenet.org/node/install/) |
| **build on it** | the protocol and the core library: [unseenet](https://github.com/unseenet/unseenet) - [Write a client](https://unseenet.org/developers/) |
| **ask something** | `unseenet.help` on Unseenet itself, or an [issue](https://github.com/unseenet/unseenet/issues) |

### The repositories

| | |
|---|---|
| **Protocol and core** | [unseenet](https://github.com/unseenet/unseenet) - the UN-RFCs, the core library, the node and the command-line client |
| **Clients** | [unseenet-gui](https://github.com/unseenet/unseenet-gui) (graphical) · [unseenet-tui](https://github.com/unseenet/unseenet-tui) (terminal) · [unseenet-mcp](https://github.com/unseenet/unseenet-mcp) (for language models, planning) |
| **Builds** | [unseenet-portable](https://github.com/unseenet/unseenet-portable) (Windows, macOS, Linux, Tor inside) · [unseenet-bootable](https://github.com/unseenet/unseenet-bootable) (boot from a stick) |
| **Ways in and out** | [unseenet-entrance](https://github.com/unseenet/unseenet-entrance) (the client in a browser) · [unseenet-gateway](https://github.com/unseenet/unseenet-gateway) (Usenet, Nostr, Matrix) |
| **On the network** | [unseenet-bots](https://github.com/unseenet/unseenet-bots) (channels with current content) · [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot) (answers in `unseenet.help`) · [unseenet-demo](https://github.com/unseenet/unseenet-demo) (something to see) |
| **The project** | [unseenet-docs](https://github.com/unseenet/unseenet-docs) (unseenet.org) · [unseenet-stats](https://github.com/unseenet/unseenet-stats) (statistics) · [.github](https://github.com/unseenet/.github) ([how the repositories work](https://github.com/unseenet/.github/blob/main/CONVENTIONS.md)) |

### Taking part

Ideas, criticism and code are welcome. Protocol changes go through the
[UN-RFC process](https://unseenet.org/spec/un-rfc-0000/) - an issue first, then
a draft; code through ordinary pull requests. Running a node or an entrance
others can use is one of the most useful things you can do: the network is
only as free as the number of people who run it.
