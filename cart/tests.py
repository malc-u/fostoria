"""Cart app tests"""
from django.test import TestCase, Client, RequestFactory, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from products.models import Product, ProductGroup
from .views import cart_view

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

    def test_basket_contents_template_not_rendered_without_cart_contents_specified_with_call(self):
        """
        Testing that adding product according to the model only
        will not result in items being added to the cart as cart_contents
        are needed from cart.contexts.py. User can be logged in product might
        be added and added to sesssion however when there is no cart_contents
        then basket-contents.html will not be rendered
        """
        client = Client()
        client.login(username='testuser', password="testpassword1")
        group = ProductGroup(id=1, name="test", display_name="display")
        group.save()
        item = Product(title="Product",
                       product_image="testing_img.jpg",
                       place="Test place",
                       has_sizes="True",
                       product_group=ProductGroup(id=1))
        item.save()
        self.client.login(username="testuser", password="testpassword1")
        session = self.client.session
        session["cart_items"] = {1:1}
        session.save()
        response = self.client.get("/cart/")
        self.assertTemplateUsed(response, 'cart.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/head.html')
        self.assertTemplateUsed(response, 'includes/header.html')
        self.assertTemplateUsed(response, 'includes/navbar-menu.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-mobile.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-desktop.html')
        self.assertTemplateUsed(response, 'includes/top-footer-sec.html')
        self.assertTemplateUsed(response, 'includes/footer.html')
        self.assertTemplateUsed(response, 'includes/scripts.html')
        self.assertTemplateNotUsed(response, 'components/basket-contents.html')

class TestCartViewtUrl(SimpleTestCase):
    """
    Testing cart_view Url
    """

    def test_cart_view_url_is_resolved(self):
        """
        Test checking if reversed url 'contact' resolved to
        'contact' view function
        """
        url = reverse('cart_view')
        self.assertEqual(resolve(url).func, cart_view)