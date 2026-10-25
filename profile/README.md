<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-dark.svg">
    <img alt="Unseenet" src="https://raw.githubusercontent.com/unseenet/unseenet/main/assets/logo-light.svg" width="360">
  </picture>
</p>

**Unseenet** is a decentralized, encrypted discussion network in the spirit of
the old Usenet and the BBSes. You run one client - from a USB stick if you like -
connect to a node over Tor, and the nodes exchange groups with each other.
Open groups are like the old Usenet; closed groups are end-to-end encrypted,
so the nodes only see noise.

The protocol is written down as RFC-style documents, the UN-RFCs, so anyone
can build nodes and clients that work together - like in the old days.

| Repository | What it is |
|---|---|
| [unseenet](https://github.com/unseenet/unseenet) | The protocol (UN-RFCs), the core library, the node and the command-line client |
| [unseenet-tui](https://github.com/unseenet/unseenet-tui) | The terminal client (moving out of unseenet) |
| [unseenet-gui](https://github.com/unseenet/unseenet-gui) | The graphical client - in a window, booted, or in a browser |
| [unseenet-portable](https://github.com/unseenet/unseenet-portable) | Builds the portable clients, Terminal and Graphical, with Tor inside |
| [unseenet-bootable](https://github.com/unseenet/unseenet-bootable) | Builds the bootable images, Terminal and Graphical, and later a node image |
| [unseenet-docs](https://github.com/unseenet/unseenet-docs) | The site [unseenet.org](https://unseenet.org), gathering the docs of every repository |
| [unseenet-entrance](https://github.com/unseenet/unseenet-entrance) | Web entrances: the graphical client in an ordinary browser |
| [unseenet-gateway](https://github.com/unseenet/unseenet-gateway) | Gateways to other networks: Usenet, Nostr, Matrix |
| [unseenet-bots](https://github.com/unseenet/unseenet-bots) | Bots that keep channels filled with current content |
| [unseenet-helpbot](https://github.com/unseenet/unseenet-helpbot) | The bot that answers questions in `unseenet.help` |
| [unseenet-stats](https://github.com/unseenet/unseenet-stats) | Statistics for the network |
| [unseenet-mcp](https://github.com/unseenet/unseenet-mcp) | An MCP server, so a language model can read and post as you (planning) |
| [unseenet-demo](https://github.com/unseenet/unseenet-demo) | Demo people, feeds and sites, made with the command-line client |

**[Documentation](https://unseenet.org)** · **[Download](https://github.com/unseenet/unseenet/releases)** · [How the repositories work](https://github.com/unseenet/.github/blob/main/CONVENTIONS.md)

Unseenet is pre-alpha: expect breaking changes. Ideas, criticism and code are
welcome - open an issue, or say hello in `unseenet.test` on Unseenet itself.
