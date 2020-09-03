"""Models of checkout app"""
import uuid
import datetime
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class OrderShippingDetails(models.Model):
    """
    Model storing all shipping details related to the order - customer, address, phone etc.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False, unique=True)
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=100, blank=False)
    first_address_line = models.CharField(max_length=75, blank=False)
    second_address_line = models.CharField(max_length=75, blank=True, null=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)

    def _generate_order_number(self):
        """
        Generating order number - function presented by Chris Zielinski during Code Insitute course
        """
  
        return uuid.uuid4().hex.upper()

    
    def save(self, *args, **kwargs):
        """
        Overriding save method to set the order number if it hasn't been set already.
        Function presented during Code Institute Course by Chris Zieinski
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.order_number
        

class OrderLineDetail(models.Model):
    """ Model containing all order details """
    order_shipping = models.ForeignKey(OrderShippingDetails, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False)
    date_ordered = models.DateField(default=datetime.date.today, blank=True)
    total = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} - {self.product.title} - {self.date_ordered} - £{self.total}'
