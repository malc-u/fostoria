"""Views of the contact app"""
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    """
    A contact view
    """
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = 
            from_email = 
            message = 

    context = {
        'contact_form': contact_form,
    }

    return render(
        request,
        "contact.html",
        context,
    )
