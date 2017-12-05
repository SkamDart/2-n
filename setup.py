try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import unittest

def test_suite():
    """
    """
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(name='2pyn',
      version='1.0',
      description='2048 AI',
      author='Cameron Dart',
      author_email='cdart2@illinois.edu',
      py_modules=['app', 'game'],
      test='tests'
      )
