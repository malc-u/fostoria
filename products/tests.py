"""Products app tests"""
from django.test import TestCase
from .models import ProductGroup, ProductGroup

# Create your tests here.
class TestProductGroup(TestCase):
    """
    ProductGroup model test
    """
    def test_product_group_can_be_saved_with_one_field_only(self):
        """
        Testing that the model can be saved
        with 1 field filled in and the other one remaining
        empty string 
        """
        test_name = ProductGroup(name="Test name")
        test_name.save()
        self.assertEqual(test_name.name, "Test name")
        self.assertEqual(test_name.display_name, "")

