from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<article_id>/', views.add_to_cart, name='add_to_cart')
]
