from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view that is returning index page """
    return render(request, 'index.html')

def about(request):
    """A vuew that returns about page"""
    return render(request, 'about.html')
