#!/usr/bin/env python3

from setuptools import setup

import configurator

long_description = open('README.rst').read() + '\n' + open('CHANGES.rst').read()

setup(
    name='python-configurator',
    version=configurator.__version__,
    description='Python module for reading configuration files in different formats',
    long_description=long_description,
    author='Hugo Shamrock',
    author_email='hugo.shamrock@gmail.com',
    url='https://github.com/HugoShamrock/python-configurator',
    packages=['configurator'],
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
    ],
)
