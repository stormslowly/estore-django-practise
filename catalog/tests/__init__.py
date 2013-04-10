import unittest

def suite():
    testsuite = unittest.TestLoader().discover('./',pattern='*.py')
    return testsuite