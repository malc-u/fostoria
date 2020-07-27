"""Products app model registration to admin """
from django.contrib import admin
from .models import ProductGroup, Product, PrintPrice, PrintSize, PricingSizes

admin.site.register(ProductGroup)
admin.site.register(Product)
admin.site.register(PrintPrice)
admin.site.register(PrintSize)
admin.site.register(PricingSizes)
