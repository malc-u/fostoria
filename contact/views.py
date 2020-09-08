"""Views of the contact app"""
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    """
    A contact view
    """
    if request.method == 'GET':
        contact_form = ContactForm()

    return render(
        request,
        "contact.html",
        context,
    )
