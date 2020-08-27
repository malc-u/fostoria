""" Home app views """
from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view that is returning index page """
    context = {
        'title': 'Index Page'
    }
    return render(request, 'index.html', context)

def about(request):
    """A vuew that returns about page"""
    context = {
        'title': 'About Page'
    }
    return render(request, 'about.html', context)
