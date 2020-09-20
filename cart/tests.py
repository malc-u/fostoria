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

    def test_basket_contents_template_rendered_with_cart_contents_specified_with_call(self):
        """
        Testing for basket-contents.html to be displayed additional info that is
        added to cart_contents context in contexts.py must be passed as well as Product instance
        cart_contents context => {'cart_items': [{'article_id': Product.id, 'qty' = content.qty,
        'product': Product.title, 'size': content.size, 'price': content.price}], 'total': content.total,
        'product_count': content.product_count}
        where content.qty = qty of Product of the X size added to the cart
        content.size = size X of Product
        content.price = price for size X od the Product
        content.total = sum of content.prices in the cart
        content.product_count = sum of content.qty in the cart
        This tests Product(id.1) being added in qty = 1, size A3 and price being £20
        """
        client = Client()
        client.login(username='testuser', password="testpassword1")
        group = ProductGroup(id=1, name="test", display_name="display")
        group.save()
        item = Product(id=1,
                       title="Product",
                       product_image="testing_img.jpg",
                       place="Test place",
                       has_sizes="True",
                       product_group=ProductGroup(id=1))
        item.save()
        self.client.login(username="testuser", password="testpassword1")
        product_size = "A3"
        product_price = 20
        session = self.client.session
        session['cart'] = {item.id :{'items_by_size': {product_size: product_price}}}
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
        self.assertTemplateUsed(response, 'components/basket-contents.html')
    

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