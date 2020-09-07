""" Home app views """
from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view that is returning index page """
    context = {
        'title': 'Index Page'
    }
    return render(request, 'index.html', context)
    