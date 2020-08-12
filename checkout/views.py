"""View of checkout application"""
from django.shortcuts import render, redirect
import stripe
from cart.contexts import cart_contents
from .forms import OrderShippingForm, PaymentForm


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

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            cart = request.session.get('cart', {})
            order_total = cart_contents(request)['total']

            try:
                customer = request.user.email
                
                charge = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = customer,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:



            return redirect('profile')

    else:
        payment_form = PaymentForm()

    context = {
        'order_total': order_total
    }
    return render(request, "checkout-payment.html", context)
