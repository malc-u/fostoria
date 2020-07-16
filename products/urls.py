"""Products app urls to be imported to main project urls"""

from django.urls import path
from products.views import Products, ProductDetails

urlpatterns = [
    path('', Products.as_view(), name='all_products'),
     path('photo/<int:pk>/', ProductDetails.as_view(), name="product-detail"),
]
