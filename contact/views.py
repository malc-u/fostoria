"""Views of the contact app"""
from django.core.mail import send_mail
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
            subject = request.POST.get('subject', '')
            from_email = request.POST.get('from_email', '')
            message = request.POST.get('message', '')

            try:
                send_mail(subject, message, from_email, [os.environ.get("EMAIL_HOST")])
            except BadHeaderError:

    context = {
        'contact_form': contact_form,
    }

    return render(
        request,
        "contact.html",
        context,
    )
