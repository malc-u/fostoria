"""Products app models"""

from django.db import models

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

    def __str__(self):
        return self.title
