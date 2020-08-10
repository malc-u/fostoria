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
            'full_name', 'first_address_line', 'second_address_line', 'town_or_city',
            'county', 'postcode', 'country', 'phone_number'
        ),
        labels = {
            'first_address_line': "First Line Of Address",
            'Second_address_line': "Second Line Of Address",
        }
