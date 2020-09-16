"""Contact app tests"""
from django.test import TestCase, Client
from .forms import ContactForm

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

# Contact form test
class TestContactForm(TestCase):
    """
    Testing Contact Form
    """

    def test_can_contact_with_all_fields(self):
        """
        Test checking if Contact Form is valid when
        all fields submitted.
        """
        form = ContactForm({
            'from_email': 'testemail@gmail.com',
            'message': 'Short message',
            'subject': 'Message subject'
            })
        self.assertTrue(form.is_valid())
