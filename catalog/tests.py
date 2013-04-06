"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from catalog.models import Category, Product

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
    
    def test_Models(self):
        category = Category();
        self.assertTrue(category)
        product = Product();
        self.assertTrue(product)
'''
from catalog.admin import ProductAdmin
from django.contrib import admin
class ModelAdminTest(TestCase):
    
    def test_ok_to_register(self):
        admin.site.register(Product, ProductAdmin)
'''