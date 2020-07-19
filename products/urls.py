"""Products app urls to be imported to main project urls"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products.as_view(), name='all_products'),
    path('lakes/', views.ProductsLakes.as_view(), name='lakes_seas'),
    path('hills/', views.ProductsHills.as_view(), name='hills'),
    path('forests/', views.ProductsForests.as_view(), name='forests'),
    path('<int:pk>/', views.ProductDetails.as_view(), name="product-detail"),
    ]
