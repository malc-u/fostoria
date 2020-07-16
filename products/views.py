"""Products app views that will be imported to project urls"""

from django.views.generic import ListView, DetailView
from .models import Product

class Products(ListView):
    """"Class that will be used as_view() and will display all products/photos"""
    template_name = "photos.html"
    context_object_name = "products"
    queryset = Product.objects.order_by('-title')
    paginate_by = 6

class ProductDetails(DetailView):
    """Class that will be used as_view() and will display detais
    for a specific product"""
    model = Product
    template_name = "details.html"
    context_object_name = "product"