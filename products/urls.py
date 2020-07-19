"""Products app urls to be imported to main project urls"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products.as_view(), name='all_products'),
    path('<int:pk>/', views.ProductDetails.as_view(), name="product-detail"),   
]
