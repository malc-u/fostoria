"""Products app urls to be imported to main project urls"""

from django.urls import path
from .views import Products, ProductsLakes, ProductsHills, ProductsForests, ProductDetails, product_search

urlpatterns = [
    path('', Products.as_view(), name='all_products'),
    path('lakes/', ProductsLakes.as_view(), name='lakes_seas'),
    path('hills/', ProductsHills.as_view(), name='hills'),
    path('forests/', ProductsForests.as_view(), name='forests'),
    path('<int:pk>/', ProductDetails.as_view(), name="product-detail"),
    path('search/', product_search, name="product_search"),
    ]
