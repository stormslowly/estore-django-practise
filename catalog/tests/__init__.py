import unittest
import os


def suite():
    testsuite = unittest.TestLoader().discover(__name__,pattern='test*.py')
    return testsuite