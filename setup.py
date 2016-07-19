#!/usr/bin/env python

import glob
from setuptools import setup
setup(
    name = "hocr_tools",
    version = "0.2",
    author = 'Thomas Breuel',
    description = 'Advanced tools for hOCR integration',
    packages = ['hocrlib'],
    scripts = [c for c in glob.glob("hocr-*")]
)
