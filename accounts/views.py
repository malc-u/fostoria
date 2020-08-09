""" Accounts app views """
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
import sweetify
from .forms import UserRegistrationForm




# Create your views here.
@csrf_protect
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

def logout(request):
    """
    Function that logs user out and redirects
    to the home page. 
    """
    auth.logout(request)
    sweetify.info(request, icon='success',
                  title='You have been successfully logged out')
    return redirect(reverse('home'))
    