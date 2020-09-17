"""Products app tests"""
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import ProductGroup, Product
from .views import product_search

# Create your tests here.
class TestProductGroup(TestCase):
    """
    ProductGroup model test
    """
    def test_product_group_can_be_saved_with_one_field_only(self):
        """
        Testing that the model can be saved
        with 1 field filled in and the other one remaining
        empty string
        """
        test_name = ProductGroup(name="Test name")
        test_name.save()
        self.assertEqual(test_name.name, "Test name")
        self.assertEqual(test_name.display_name, "")

class TestProduct(TestCase):
    """
    Product model test
    """
    def test_product_name_returned(self):
        """Testing that correct product title is returned."""
        test_product = Product(title="Test product")
        self.assertEqual(test_product.title, "Test product")

class TestProductSearchUrl(SimpleTestCase):
    """
    Testing product_search Url
    """

    def test_product_search_url_is_resolved(self):
        """
        Test checking if reversed url 'product_search' resolved to
        'product_search' function
        """
        url = reverse('product_search')
        self.assertEqual(resolve(url).func, product_search)
