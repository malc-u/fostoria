"""Products app urls to be imported to main project urls"""

from django.urls import path
from products.views import Products

urlpatterns = [
    path('', Products.as_view(), name='all_products'),
]
