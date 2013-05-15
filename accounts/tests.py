"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
from accounts import views


class SimpleTest(TestCase):

    def test_get_login_should_be_ok(self):
        register_path =reverse('register');
        self.assertEqual('/accounts/register/', register_path);
        
        login_path = reverse('login');
        self.assertEqual('/accounts/login/', login_path)


    def test_login_web_page(self):
        
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)