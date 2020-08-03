"""Urls for an app called CART """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<article_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<article_id>/', views.update_cart, name='update_cart')
]
