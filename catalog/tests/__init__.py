import unittest

def suite():
    testsuite = unittest.TestLoader().discover('./',pattern='*.py')
    print "runed"
    return testsuite