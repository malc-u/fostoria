"""View of checkout application"""
from django.shortcuts import render
from .forms import OrderShippingForm

# Create your views here.

def checkout_delivery_view(request):

    if request.method == 'POST':
        order_shipping_form = OrderShippingForm(request.POST)
    else:
        order_shipping_form = OrderShippingForm()

    return render(request, template, context)
