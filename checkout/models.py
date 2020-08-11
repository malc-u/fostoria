"""Models of checkout app"""
import datetime
from django.db import models
from django.contrib.auth.models import User

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
        return f"{self.id}-{self.customer}"
