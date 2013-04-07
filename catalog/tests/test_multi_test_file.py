from django.test import TestCase

class Just_for_Test(TestCase):
    """docstring for Just_for_Test"""
    def test_fail(self):
        self.fail("great fail")

