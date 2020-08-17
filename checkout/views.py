"""View of checkout application"""
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import stripe
import sweetify
from cart.contexts import cart_contents
from .forms import OrderShippingForm, PaymentForm


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required
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


@login_required
def checkout_payment_view(request):

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            order_total = cart_contents(request)['total']

            try:
                customer = request.user.email
                
                charge = stripe.Charge.create(
                    amount = int(order_total * 100),
                    currency = "GBP",
                    description = customer,
                    card = payment_form.cleaned_data['stripe_id'],
                )
                if charge:
                    sweetify.success(
                    request,
                    title="Payment processed sucessfully. Thank you.",
                    icon="success")
                    del request.session['cart']
                    return redirect(reverse('all_products'))

            except stripe.error.CardError:
                sweetify.error(
                    request,
                    title="Something went wrong with the payment, please try again.",
                    icon="error")
            
            except stripe.error.RateLimitError:
                sweetify.error(
                    request,
                    title="Our servers couldn't process the payment, please try again.",
                    icon="warning")
            except stripe.error.InvalidRequestError:
                sweetify.error(
                    request,
                    title="Payment error, please try again.",
                    icon="warning")
            except stripe.error.AuthenticationError:
                sweetify.error(
                    request,
                    title="Authentication error, please try again.",
                    icon="warning")
            except stripe.error.APIConnectionError:
                sweetify.error(
                    request,
                    title="Server communication error, please try again.",
                    icon="warning")

            return redirect('profile')

    else:
        payment_form = PaymentForm()

    context = {
        'order_total': order_total,
        'payment_form': payment_form,
    }
    return render(request, "checkout-payment.html", context)
