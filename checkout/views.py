"""View of checkout application"""
from django.shortcuts import render, redirect
from .forms import OrderShippingForm

# Create your views here.

def checkout_delivery_view(request):

    if request.method == 'POST':
        order_shipping_form = OrderShippingForm(request.POST)
        if order_shipping_form.is_valid():
            order_shipping = order_shipping_form.save(commit=False)
            order_shipping.customer = request.user
            order_shipping.save()
            return redirect("payment")
    else:
        order_shipping_form = OrderShippingForm()

    context = {
        'order_shipping_form': order_shipping_form
    }
    return render(request, "checkout-delivery.html", context)


def checkout_payment_view(request):

    return render(request, "checkout-payment.html", context)
    