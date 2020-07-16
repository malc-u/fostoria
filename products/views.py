"""Products app views that will be imported to project urls"""

from django.views.generic import ListView
from .models import Product

class Products(ListView):
    """"Class that will be used as_view() and will display all products/photos"""
    template_name = "photos.html"
    context_object_name = "products"
    queryset = Product.objects.order_by('-title')
    paginate_by = 6
