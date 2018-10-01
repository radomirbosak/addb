#!/usr/bin/env
# -*- coding: utf-8 -*-

import os

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'addb', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)


setup(
    name='addb',
    entry_points={
        'console_scripts': ['addb = addb.main:main', ],
    },
    install_requires=[
        "pyxdg",
    ],
    packages=['addb'],
    version=about['__version__'],
)
