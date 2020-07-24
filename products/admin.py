from django.contrib import admin
from .models import ProductGroup, Product, PrintPrice, PrintSize, PricingSizes

# Register your models here.
admin.site.register(ProductGroup)
admin.site.register(Product)
admin.site.register(PrintPrice)
admin.site.register(PrintSize)
admin.site.register(PricingSizes)