"""View of checkout application"""
from django.shortcuts import render, redirect
from .forms import OrderShippingForm

# Create your views here.

def checkout_delivery_view(request):

    if request.method == 'POST':
        order_shipping_form = OrderShippingForm(request.POST)
        if order_shipping_form.is_valid():

            return redirect("checkout_payment")
    else:
        order_shipping_form = OrderShippingForm()

    context = {
        'order_shipping_form': order_shipping_form
    }
    return render(request, "checkout-shipping.html", context)
