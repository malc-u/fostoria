"""Accounts app urls that are imported to main project urls"""
from django.contrib.auth import views as auth
from django.urls import path
from .views import register_view, logout, profile_view

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', auth.LoginView.as_view(template_name='login.html',
                                          redirect_authenticated_user=True),
         name="login"),
    path('logout/', logout, name="logout"),
]
