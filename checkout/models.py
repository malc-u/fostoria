"""Models of checkout app"""
import datetime
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class OrderShippingDetails(models.Model):
    """
    Model storing all shipping details related to the order - customer, address, phone etc.
    """
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=100, blank=False)
    first_address_line = models.CharField(max_length=75, blank=False)
    second_address_line = models.CharField(max_length=75, blank=True, null=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)



    def __str__(self):

        return f'{self.id}-{self.order_number}'
        

class OrderLineDetail(models.Model):
    """ Model containing all order details """
    order_shipping = models.ForeignKey(OrderShippingDetails, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)
    date_ordered = models.DateField(default=datetime.date.today, blank=True)
    total = models.IntegerField(blank=False)

    def __str__(self):
        return f'{self.quantity} - {self.product.title} - {self.date_ordered} - £{self.total}'
