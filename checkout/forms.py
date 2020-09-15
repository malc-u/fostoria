"""Forms for checkout app"""
from django import forms
from .models import OrderShippingDetails

class OrderShippingForm(forms.ModelForm):
    """
    Form that is rendered for user to fill in shipping details during checkout
    """
    class Meta:
        model = OrderShippingDetails
        fields = (
            'full_name',
            'first_address_line',
            'second_address_line',
            'town_or_city',
            'county',
            'postcode',
            'country',
            'phone_number'
        )
        labels = {
            'first_address_line': "First line of address",
            'second_address_line': "Second line of address",
        }

class PaymentForm(forms.Form):
    """
    Form that is rendered for user to process the card payment. It renders
    all required fields for card payment processing.

    This form was presented during Code Institute course but it is modified by me
    to display months from January until December (inclusive)
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2035)]

    credit_card_number = forms.CharField(
        max_length=16,
        label='Credit card number',
        required=False
    )
    cvv = forms.CharField(
        max_length=3,
        label='Security code (CVV)',
        required=False
    )
    expiry_month = forms.ChoiceField(
        label='Expiry Month',
        choices=MONTH_CHOICES,
        required=False
    )
    expiry_year = forms.ChoiceField(
        label='Expiry Year',
        choices=YEAR_CHOICES,
        required=False
    )
    stripe_id = forms.CharField(
        widget=forms.HiddenInput()
    )
