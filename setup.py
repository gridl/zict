#!/usr/bin/env python

import os
from setuptools import setup

setup(name='zdict',
      version='0.0.1',
      description='Mutable mapping tools',
      url='http://github.com/mrocklin/zdict/',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='mutable mapping dict',
      packages=['zdict'],
      install_requires=[],
      long_description=(open('README.rst').read() if os.path.exists('README.rst')
                        else ''),
      zip_safe=False)