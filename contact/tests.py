"""Contact app tests"""
from django.test import TestCase, Client

# View test
class TestContactView(TestCase, Client):
    """
    Testing "contact" view.
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_contact_page(self):
        """
        Test checking if view contact is sucessfully loaded (status 200)
        when URL ("/contact/") called.
        """
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)

    def test_get_contact_template(self):
        """
        Test checking if correct template is used ('contact.html')
        when URL ("/contact/") called.
        """
        response = self.client.get("/contact/")
        self.assertTemplateUsed(response, 'contact.html')
        self.assertTemplateNotUsed(response, 'products.html')
