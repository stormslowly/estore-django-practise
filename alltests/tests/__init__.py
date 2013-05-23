import os
import unittest

def suite():
    testsuite = unittest.TestLoader().discover('./' ,pattern='*test*.py')
    return testsuite
