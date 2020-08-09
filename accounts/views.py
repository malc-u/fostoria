""" Accounts app views """
from django.shortcuts import render
from .forms import UserRegistrationForm


# Create your views here.
def register_view(request):
    """
    View for users to register a new account.
    Renders registration form and once submit button clicked
    checks if it's valid. Yes - saves user, No - highlights errors.
    """

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)
    