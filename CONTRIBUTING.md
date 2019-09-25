# Contributing to macaddress

Thanks for taking an interest in this awesome little project. We love
to bring new members into the community, and can always use the help.

## Resources
* Task tracking and Bug reports: [GitHub](https://github.com/GhostofGoes/macaddress/issues)
* Discussion: the [Python Discord server](https://discord.gg/python)


# Code requirements
* Must work under all supported Python versions (3.6+)
* Must work on all supported platforms (if applicable)
* Try to match the general code style (loosely PEP8)
* Be respectful. Memes, references, and jokes are ok. Explicit language
(cursing/swearing), NSFW text/content, or racism are NOT ok.

## Checklist before submitting a pull request
* [ ] All tests run and pass locally
    * [ ] `tox`
    * [ ] `tox -e check`
* [ ] Update the [CHANGELOG](CHANGELOG.md) (For non-trivial changes, e.g. changing functionality or adding tests)
* [ ] Add your name to the contributors list in the [README](README.md)

## Checklist before a Pull Request will be merged
* [ ] *All* TravisCI tests pass
* [ ] Appveyor tests pass
* [ ] Code has been reviewed by at least one maintainer


# Where to contribute

## Good for beginners
* Bug reports!
* Documentation (including fixes for grammar and spelling)
* Improving and adding tests (e.g. to improve coverage)

# Getting started
1. Create your own fork of the code through GitHub web interface ([Here's a Guide](https://gist.github.com/Chaser324/ce0505fbed06b947d962))
2. Clone the fork to your computer. This can be done using the
[GitHub desktop](https://desktop.github.com/) GUI , `git clone <fork-url>`,
or the Git tools in your favorite editor or IDE.
3. Create and checkout a new branch in the fork with either your username (e.g. "ghostofgoes"),
or the name of the feature or issue you're working on (e.g. "openbsd-support").
Again, this can be done using the GUI, your favorite editor, or `git checkout -b <branch> origin/<branch>`.
4. Install the developer tools, package, and pre-commit hooks:
    ```bash
    python -m pip install --user -U tox
    python -m pip install -e .
    ```
5. Setup and run the tests:
    ```bash
    # Run code quality checks
    tox -e check

    # Run the tests
    tox
    ```
6. Write some code! Git commit messages should information about what changed,
and if it's relevant, the rationale (thinking) for the change.
7. Follow the checklist
8. Submit a pull request!


# Bug reports
Filing a bug report:

1. Answer these questions:
    * [ ] What version of `macaddress` are you using? (`pip list | grep macaddress`)
    * [ ] What operating system and processor architecture are you using?
    * [ ] What version of Python are you using?
    * [ ] What did you do?
    * [ ] What did you expect to see?
    * [ ] What did you see instead?
2. Put any excessive output into a [GitHub Gist](https://gist.github.com/) and include a link in the issue.
3. Tag the issue with "Bug"

**NOTE**: If the issue is a potential security vulnerability, do *NOT* open an issue!
Instead, email: ghostofgoes(at)gmail(dot)com

# Features and ideas
Ideas for features or other things are welcomed. Open an issue on GitHub
detailing the idea, and tag it appropriately (e.g. "Feature" for a new feature).
