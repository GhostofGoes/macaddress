If `twine` isn't installed, get it: `python -m pip install --user -U twine`

1. Increment version number in `macaddress/macaddress.py`
2. Update CHANGELOG header from UNRELEASED to the version and add the date
3. Run static analysis checks (`tox -e check`)
4. Run the test suite on the main supported platforms (`tox`)
    a) Windows
    b) Ubuntu
    c) CentOS
    d) OSX
5. Ensure a pip install from source works on the main platforms:
```bash
pip install https://github.com/ghostofgoes/macaddress/archive/master.tar.gz
```
6. Clean the environment: `bash ./scripts/clean.sh`
7. Build the wheels
```bash
python setup.py sdist bdist_wheel --universal
```
8. Upload the wheels
```bash
twine upload dist/*
```
9. Create a tagged release on GitHub including:
    a) The relevant section of the CHANGELOG in the body
    b) The source and binary wheels
10. Edit the package name in setup.py to `get-mac`, and re-run
steps 7 and 8 (build and upload), since people apparently don't check
their dependencies and ignore runtime warnings.
11. Announce the release in the normal places
