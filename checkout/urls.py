""" Checkout app urls to be imported to main project urls """
from django.urls import path
from . import views

urlpatterns = [
    path('delivery/', views.checkout_delivery_view, name='delivery'),
    path('payment/', views.checkout_payment_view, name='payment'),
]
