"""About app views"""
from django.shortcuts import render

# Create your views here.

def about(request):
    """A view that returns about page"""
    context = {
        'title': 'About Page'
    }
    return render(request, 'about.html', context)
