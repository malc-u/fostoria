""" Accounts app views """
from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
import sweetify
from checkout.models import OrderLineDetail
from .forms import UserRegistrationForm, UserUpdateForm


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
        "title": 'Registration Page',
    }
    return render(request, 'register.html', context)

def logout_view(request):
    """
    Function that logs user out and redirects
    to the home page.
    """
    auth.logout(request)
    sweetify.info(request, icon='success',
                  title='You have been successfully logged out')
    return redirect(reverse('home'))


@login_required
def profile_view(request):
    """
    Renders profile page for user with a form to update
    their information, already filled out with their current
    data.
    """
    user = User.objects.get(username=request.user)
    order_line_record = OrderLineDetail.objects.filter(
        order_shipping__customer_id=user.id).order_by("-date_ordered")

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            sweetify.success(
                request, icon='success',
                title="Your details have been updated."
            )
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'form': form,
        'title': 'Profile Page',
        'order_line_record': order_line_record,
    }

    return render(request, 'profile.html', context)
    