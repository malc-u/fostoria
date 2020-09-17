"""Home app tests"""
from django.test import TestCase, Client

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
