#!/usr/bin/env python
"""
Run all the vimzk python unit tests.

Combining code from
https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory (slaughter98)
https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory (Russell Dias)

"""
import os
import unittest


def run_all_tests():
    """Load and run all the tests."""
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(os.path.realpath(__file__)))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_all_tests()
