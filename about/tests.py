"""About app tests"""
from django.test import TestCase, Client

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
        Test checking if correct template is used ('about.html')
        when URL ("/about/") called.
        """
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateNotUsed(response, 'contact.html')
