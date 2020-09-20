""" Checkout app tests"""
from django.test import TestCase
from .forms import PaymentForm

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
