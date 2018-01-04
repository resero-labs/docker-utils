#!/usr/bin/env bash
# vim: filetype=sh:

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd ..

pip install wheel twine
python setup.py bdist_wheel -d dist
twine upload -r pypi dist/*
