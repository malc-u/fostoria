from django.contrib import admin
from .models import ProductGroup, Product

# Register your models here.
admin.site.register(ProductGroup)
admin.site.register(Product)