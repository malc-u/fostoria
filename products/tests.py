"""Products app tests"""
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .models import ProductGroup, Product
from .views import (product_search,
                    Products,
                    ProductsForests,
                    ProductsHills,
                    ProductsLakes)

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

class TestAllClassBasedViewsUrls(SimpleTestCase):
    """
    Testing some class based views Urls
    """
    def test_lakes_seas_url_is_resolved(self):
        """
        Test checking if reversed url 'lakes_seas' resolved to
        ProductsLakes view' class
        """
        url = reverse('lakes_seas')
        self.assertEqual(resolve(url).func.view_class, ProductsLakes)

    def test_forests_url_is_resolved(self):
        """
        Test checking if reversed url 'forests' resolved to
        ProductsHills view' class
        """
        url = reverse('forests')
        self.assertEqual(resolve(url).func.view_class, ProductsForests)

    def test_hills_url_is_resolved(self):
        """
        Test checking if reversed url 'hills' resolved to
        ProductsHills view' class
        """
        url = reverse('hills')
        self.assertEqual(resolve(url).func.view_class, ProductsHills)

    def test_all_products_url_is_resolved(self):
        """
        Test checking if reversed url 'all_products' resolved to
        Products view' class
        """
        url = reverse('all_products')
        self.assertEqual(resolve(url).func.view_class, Products)

class TestProductsView(TestCase, Client):
    """
    Testing Products view (all_products)
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_all_products_page(self):
        """
        Test checking if register_view is sucessfully loaded (status 200)
        when URL ("/photos/") called.
        """
        response = self.client.get("/photos/")
        self.assertEqual(response.status_code, 200)

    def test_get_all_products_template(self):
        """
        Test checking if correct template is used ('register.html' and all
        others that were included on this template) when URL ("/accounts/register/") called.
        """
        response = self.client.get("/photos/")
        self.assertTemplateUsed(response, 'photos.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/head.html')
        self.assertTemplateUsed(response, 'includes/header.html')
        self.assertTemplateUsed(response, 'includes/navbar-menu.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-mobile.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-desktop.html')
        self.assertTemplateUsed(response, 'includes/top-footer-sec.html')
        self.assertTemplateUsed(response, 'includes/footer.html')
        self.assertTemplateUsed(response, 'includes/scripts.html')
        self.assertTemplateNotUsed(response, 'contact.html')
