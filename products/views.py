"""Products app views that will be imported to project urls"""
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib import messages
from .models import Product, PricingSizes


class Products(ListView):
    """"Class that will be used as_view() and will display all products/photos"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.order_by('-title')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context['group'] = "Gallery"
        return context

class ProductDetails(DetailView):
    """Class that will be used as_view() and will display detais
    for a specific product"""
    model = Product
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetails, self).get_context_data(**kwargs)
        priced_sizes = PricingSizes.objects.all()
        context['priced_sizes'] = priced_sizes
        context['title'] = "- Lakes & Seas Gallery"
        return context


class ProductsLakes(ListView):
    """"Class that will be used as_view() and will display products/photos assigned to
    product_group: lakes_seas"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.filter(product_group__name='lakes_seas').order_by('title')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProductsLakes, self).get_context_data(**kwargs)
        context['group'] = "Lakes & Seas"
        context['title'] = "- Lakes & Seas Gallery"
        return context

class ProductsHills(ListView):
    """"Class that will be used as_view() and will display products/photos assigned to
    product_group: fields_hills"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.filter(product_group__name='fields_hills').order_by('title')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProductsHills, self).get_context_data(**kwargs)
        context['group'] = "Fields & Mountains"
        context['title'] = "- Fields & Mountains Gallery"
        return context

class ProductsForests(ListView):
    """"Class that will be used as_view() and will display products/photos assigned to
    product_group: forests"""
    model = Product
    template_name = "photos.html"
    queryset = Product.objects.filter(product_group__name='forests').order_by('-title')
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProductsForests, self).get_context_data(**kwargs)
        context['group'] = "Forests"
        context['title'] = "- Forests Gallery"
        return context

def product_search(request):
    """ View allowing searching products using Product title or place"""
    query = request.GET.get('q')
    if query:
        query_group = Q(title__icontains=query) | Q(place__icontains=query)
        products = Product.objects.filter(query_group)

        if not products:
            messages.error(request, 'There is no photos matching your search criteria')
            return redirect(reverse('all_products'))

        context = {
            'products': products,
            'query': query,
            'title': "- Photos search",
        }
        return render(request, "photos-search.html", context)

    messages.error(request, 'Search criteria is missing, please try again.')
    return redirect(reverse('all_products'))
