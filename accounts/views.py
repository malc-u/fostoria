""" Accounts app views """
from django.shortcuts import render, redirect
import sweetify
from .forms import UserRegistrationForm


# Create your views here.
def register_view(request):
    """
    View for users to register a new account.
    Renders registration form and once submit button clicked
    checks if it's valid. Yes - saves user, No - highlights errors.
    """
    if request.user.is_authenticated:
        sweetify.info(request,
                     title="You are already logged in.",
                     icon="info")
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.info(request,
                             title="You have been successfully registered.",
                             icon="success")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)
    