#!/usr/bin/env python3

from setuptools import setup

from macaddress import __version__


# Build the page that will be displayed on PyPI from the README and CHANGELOG
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()
long_description += "\n\n"
with open("CHANGELOG.md", encoding="utf-8") as f:
    long_description += f.read()


setup(
    name="macaddress",
    version=__version__,
    author="Christopher Goes",
    author_email="ghostofgoes@gmail.com",
    description="Get MAC addresses of remote hosts and local interfaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GhostofGoes/macaddress",
    project_urls={
        "Discord server": "https://discord.gg/python",
        "Issue tracker": "https://github.com/GhostofGoes/macaddress/issues",
    },
    license="MIT",
    packages=["macaddress"],
    zip_safe=True,
    python_requires=">=3.6",
    keywords=[
        "mac",
        "mac-48",
        "macaddress",
        "mac-address",
        "get-mac",
        "getmac",
        "ethernet",
        "networking",
        "network",
        "layer2",
        "layer-2",
        "802.3",
    ],
    install_requires=["getmac"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Systems Administration",
        "Topic :: System :: Networking",
        "Topic :: Utilities",
    ],
)
