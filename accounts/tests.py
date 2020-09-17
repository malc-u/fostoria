"""Accounts app tests"""
from django.test import TestCase, Client

# Create your tests here.
class TestRegisterView(TestCase, Client):
    """
    Testing register_view
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_register_page(self):
        """
        Test checking if register_view is sucessfully loaded (status 200)
        when URL ("/accounts/register/") called.
        """
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
    

