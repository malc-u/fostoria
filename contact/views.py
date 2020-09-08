"""Views of the contact app"""
import os
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, reverse
import sweetify
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
            subject = request.POST.get('subject', '')
            from_email = request.POST.get('from_email', '')
            message = request.POST.get('message', '')

            try:
                send_mail(subject, message, from_email, [os.environ.get("EMAIL_HOST")])
            except BadHeaderError:
                sweetify.error(
                    request,
                    title="Server communication error, please try again.",
                    icon="warning")
            else:
                sweetify.success(
                    request,
                    title="Message sent.",
                    icon="success")
                return redirect(reverse('contact'))

    context = {
        'contact_form': contact_form,
        'title': 'Contact'
    }

    return render(
        request,
        "contact.html",
        context,
    )
