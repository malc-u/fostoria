"""Products app models"""

from django.db import models
from django.urls import reverse

class ProductGroup(models.Model):
    """"Model for groups that products will be assigned to"""
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)

    def __str__(self):
        """Str method returning name"""
        return self.name

    def get_display_name(self):
        """Model method returning display name """
        return self.display_name

class Product(models.Model):
    """ Model for product instances """

    title = models.CharField(max_length=254)
    place = models.CharField(max_length=254)
    product_image = models.ImageField(blank=False)
    product_group = models.ForeignKey('ProductGroup',
                                      blank=False, null=False, on_delete=models.PROTECT)
    has_sizes = models.BooleanField(default=True, null=False, blank=False)

    def get_absolute_url(self):
        """Method to tell Django how to calculate the canonical URL for an object.
            https://docs.djangoproject.com/en/3.0/ref/models/instances/ """
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class PrintPrice(models.Model):
    """Class that will allow admin set the print sizes"""
    print_price = models.IntegerField(blank=False, null=False)
    print_sizes = models.ManyToManyField('PrintSize', through='PricingSizes')

    def __str__(self):
        return '{self.print_price}'.format(self=self)



class PrintSize(models.Model):
    """Class that will allow admin set the prices for prints"""
    print_size = models.CharField(max_length=120)
    print_prices = models.ManyToManyField('PrintPrice', through='PricingSizes')

    def __str__(self):
        return self.print_size


class PricingSizes(models.Model):
    """Through Class that allow to combine prices with sizes"""
    print_size = models.ForeignKey('PrintSize', on_delete=models.CASCADE)
    print_price = models.ForeignKey('PrintPrice', on_delete=models.CASCADE)
