""" Checkout app tests"""
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .forms import PaymentForm
from .views import checkout_delivery_view

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
