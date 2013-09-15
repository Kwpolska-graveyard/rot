#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='rot',
      version='0.1.0',
      description='INSERT TAGLINE HERE.',
      keywords='rot',
      author='Kwpolska',
      author_email='kwpolska@kwpolska.tk',
      url='https://github.com/Kwpolska/rot',
      license='3-clause BSD',
      long_description=open('./docs/README.rst').read(),
      platforms='any',
      zip_safe=False,
      test_suite='tests',
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3'],
      packages=['rot'])
      #requires=['stuff'],
      #scripts=['bin/rot'],
      #data_files=[('file', ['dest']),],
