"""Products app model registration to admin """
from django.contrib import admin
from .models import OrderShippingDetails, OrderLineDetail

admin.site.register(OrderShippingDetails)
admin.site.register(OrderLineDetail)
