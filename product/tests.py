from django.test import TestCase, SimpleTestCase


# Create your tests here.

class ProductsTests(SimpleTestCase):
    #databases = ['default']
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)



class BrandTests(SimpleTestCase):
    #databases = ['default']
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/products/brands')
        self.assertEqual(response.status_code,200)

