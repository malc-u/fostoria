"""Views of the contact app"""
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    """
    A contact view
    """

    return render(
        request,
        "contact.html",
        context,
    )
