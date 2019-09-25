
**WORK IN PROGRESS - NOT YET STABLE**

Modern Pythonic interface for working with MAC addresses. It provides 
object-oriented facilities for address discovery, parsing, and validation.


## Installation
**NOT YET RELEASED** Stable release from PyPI

```bash
pip install macaddress
```

Latest development version

```bash
pip install https://github.com/ghostofgoes/macaddress/archive/master.tar.gz
```


## Should you use this package?
If you only need the addresses of network interfaces, have a limited set
of platforms to support, and are able to handle C-extension modules, then
you should instead check out the excellent [netifaces](https://pypi.org/project/netifaces/)
package by Alastair Houghton. It is significantly faster, well-maintained,
and has been around much longer than this has. Another great option that
fits these requirements is the well-known and battle-hardened
[psutil](https://github.com/giampaolo/psutil) package by Giampaolo Rodola.

If the only system you need to run on is Linux, you can run as root,
and C-extensions modules are fine, then you should instead check out the
[arpreq](https://pypi.org/project/arpreq/) package by Sebastian Schrader.
It can be significantly faster, especially in the case of hosts that
don't exist (at least currently).

If you want to use `psutil`, `scapy`, or `netifaces`, I have examples of how to do
so in a [GitHub Gist](https://gist.github.com/GhostofGoes/0a8e82930e75afcefbd879a825ba4c26).


## Python examples
```python
# TODO
```

## Terminal examples
```bash
TODO
```

## Background and history
The Python standard library has a robust set of networking functionality,
such as `urllib`, `ipaddress`, `ftplib`, `telnetlib`, `ssl`, and more.
Imagine my surprise, then, when I discovered there was not a way to get a
seemingly simple piece of information: a MAC address. This package was born
out of a need to get the MAC address of hosts on the network without
needing admin permissions, and a cross-platform way get the addresses
of local interfaces.

This project was born April 2019 from my original project, `getmac`.
The goal of this is to provide a robust set of parsing and validation
facilities, as well as a better and more Pythonic interface that
works with modern features like `asyncio` and type annotations.
Further, the fact that there is no `macaddress` module has been
bothering me for years :)

## Contributing
Contributors are more than welcome!
See the [contribution guide](CONTRIBUTING.md) to get started,
and checkout the [todo list](TODO.md) for a full list of tasks and bugs.

Before submitting a PR, please make sure you've completed the
[pull request checklist](CONTRIBUTING.md#Code_requirements)!

The [Python Discord server](https://discord.gg/python) is a good place
to ask questions or discuss the project (Handle: @KnownError).

### Contributors
* Christopher Goes (@ghostofgoes) - Author and maintainer

## License
MIT. Feel free to copy, modify, and use to your heart's content.
Please note and respect the BSD licencing for the parsing code,
as it was originally derived from `netaddr` (see `netaddr-LICENSE` 
or the code file header comment for details).
