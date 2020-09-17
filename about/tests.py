"""About app tests"""
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from .views import about

# Create your tests here.
class TestAboutView(TestCase, Client):
    """
    Testing "about" view.
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_about_page(self):
        """
        Test checking if view about is sucessfully loaded (status 200)
        when URL ("/about/") called.
        """
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_get_about_template(self):
        """
        Test checking if correct template is used ('about.html' and all
        others that were included on this template) when URL ("/about/") called.
        """
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/head.html')
        self.assertTemplateUsed(response, 'includes/header.html')
        self.assertTemplateUsed(response, 'includes/navbar-menu.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-mobile.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-desktop.html')
        self.assertTemplateUsed(response, 'components/about-faq.html')
        self.assertTemplateUsed(response, 'includes/top-footer-sec.html')
        self.assertTemplateUsed(response, 'includes/footer.html')
        self.assertTemplateUsed(response, 'includes/scripts.html')
        self.assertTemplateNotUsed(response, 'contact.html')


# URL test
class TestAboutUrl(SimpleTestCase):
    """
    Testing About Url
    """

    def test_about_url_is_resolved(self):
        """
        Test checking if reversed url 'about' resolved to
        'about' view function
        """
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)
