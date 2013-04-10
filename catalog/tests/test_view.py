from django.test import TestCase
from catalog.views import show_product
from django.http.request import HttpRequest
from catalog.models import Product

class test_show_product(TestCase):
    """ for Just_for_Test"""
    
    def setUp(self):
        p = Product()
        p.name = 'lays'
        p.slug = 'lays'
        p.price = 10.00
        p.quantity= 1
        p.save();
    def tearDown(self):
        p = Product.objects.filter(name='lays')[0]
        p.delete()
    
    def test_product_view(self):
        request = HttpRequest()
        response = show_product(request,u'lays')
        self.assertTrue(response)
        self.assertInHTML('<h1>lays</h1>',
                          response.content, 1,
                          "response don't has <h1>product name<h1>")
        self.assertTrue(-1)
