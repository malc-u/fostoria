from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from products.models import Product

# Create your tests here.
class TestCartView(TestCase):
    """
    Testing cart_view
    """

    def setUp(self):
        """
        Create client to conduct test for not logged in user,
        accessing RequestFactory() - creating instance of user
        for testing
        """
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testpassword1"
        )

    def test_redirect_with_empty_cart(self):
        """
        Testing cart view when user not logged
        in - /cart/ working as it should (status 200).
        """
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)

    
    def test_response_status_200(self):
        """
        Testing cart view when user logged in -
        /cart/ working as it should.
        """

        client = Client()
        client.login(username='testuser', password="testpassword1")

        response = client.get('/cart/')
        self.assertEqual(response.status_code, 200)
