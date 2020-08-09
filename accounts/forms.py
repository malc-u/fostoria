"""Forms that will allow new user to register"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    """
    Registration form - this is based on Django User model.
    https://docs.djangoproject.com/en/3.0/topics/auth/default/
    """
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

