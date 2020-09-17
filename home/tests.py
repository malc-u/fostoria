"""Home app tests"""
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from .views import index

# Create your tests here.
class TestIndexView(TestCase, Client):
    """
    Testing "index" view in a home app.
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_index_page(self):
        """
        Test checking if view index is sucessfully loaded (status 200)
        when URL ("/") called.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


    def test_get_index_template(self):
        """
        Test checking if correct template is used ('index.html' and all
        others that were included on this template) when URL ("/") called.
        """
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'index.html')
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

# URL test
class TestHomeUrl(SimpleTestCase):
    """
    Testing Home Url
    """

    def test_home_url_is_resolved(self):
        """
        Test checking if reversed url 'home' resolved to
        'index' view function
        """
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)
