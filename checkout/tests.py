""" Checkout app tests"""
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .forms import PaymentForm
from .views import checkout_delivery_view, checkout_payment_view


# Create your tests here.
class TestPaymentForm(TestCase):
    """
    Testing Payment Form
    """
    def test_cannot_use_cvv_longer_than_three_digits(self):
        """
        Confirming that more than 1 field (username in this case) is needed to create new user
        """
        form = PaymentForm({'cvv': '1234'})
        self.assertFalse(form.is_valid())

class TestDeliveryUrl(SimpleTestCase):
    """
    Testing Delivery Url
    """
    def test_delivery_url_is_resolved(self):
        """
        Test checking if reversed url 'delivery' resolved to
        'checkout_delivery_view' function
        """
        url = reverse('delivery')
        self.assertEqual(resolve(url).func, checkout_delivery_view)

class TestPaymentUrl(SimpleTestCase):
    """
    Testing Payment Url
    """
    def test_payment_url_is_resolved(self):
        """
        Test checking if reversed url 'payment' resolved to
        'checkout_payment_view' function
        """
        url = reverse('payment')
        self.assertEqual(resolve(url).func, checkout_payment_view)

class TestCheckoutDeliveryView(TestCase, Client):
    """
    Testing "contact" view.
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()


    def test_cannot_get_checkout_delivery_page_not_logged_in(self):
        """
        Test checking if view checkout_delivery_view is denied
        (status 302) when URL ("/checkout/delivery/") called - user not logged in...
        """
        response = self.client.get("/checkout/delivery/")
        self.assertEqual(response.status_code, 302)
