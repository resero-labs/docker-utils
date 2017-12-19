#!/usr/bin/env python
import codecs
from os import path
import sys
import versioneer

from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


requires = []


setup_options = dict(
    name='dockerutils',
    cmdclass=versioneer.get_cmdclass(),
    version=versioneer.get_version(),
    description='Docker Utilities/Patterns for Python Projects',
    long_description=long_description,
    author='Daniel Rapp',
    url='https://github.com/rappdw/docker-utils.git',
    scripts=['bin/build-image', 'bin/publish-image',
             'bin/run-image', 'bin/genversion', 'bin/transfer-image'],
    packages=find_packages(exclude=['tests*']),
    license="MIT License",
    python_requires='>=3.6',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ),
)

setup(**setup_options)
