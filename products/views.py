"""Products app views that will be imported to project urls"""

from django.views.generic import ListView, DetailView
from .models import Product

class Products(ListView):
    """"Class that will be used as_view() and will display all products/photos"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.order_by('-title')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context['group'] = "Gallery"
        return context

class ProductDetails(DetailView):
    """Class that will be used as_view() and will display detais
    for a specific product"""
    model = Product
    template_name = "details.html"
    context_object_name = "product"


class ProductsLakes(ListView):
    """"Class that will be used as_view() and will display products/photos assigned to
    product_group: lakes_seas"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.filter(product_group__name='lakes_seas').order_by('title')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductsLakes, self).get_context_data(**kwargs)
        context['group'] = "Lakes & Seas"
        context['title'] = "Lakes & Seas Gallery"
        return context

class ProductsHills(ListView):
    """"Class that will be used as_view() and will display products/photos assigned to
    product_group: lakes_seas"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.filter(product_group__name='fields_hills').order_by('title')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductsHills, self).get_context_data(**kwargs)
        context['group'] = "Fields & Mountains"
        context['title'] = "Fields & Mountains Gallery"
        return context

class ProductsForests(ListView):
    """"Class that will be used as_view() and will display products/photos assigned to
    product_group: lakes_seas"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.filter(product_group__name='forests').order_by('title')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(ProductsForests, self).get_context_data(**kwargs)
        context['group'] = "Forests"
        context['title'] = "Forests Gallery"
        return context