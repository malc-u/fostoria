"""Products app views that will be imported to project urls"""

from django.views.generic import ListView
from .models import Product

class Products(ListView):
    template_name = "photos.html"
    context_object_name = "products"
    queryset = Product.objects.order_by('-title')
    paginate_by = 6
