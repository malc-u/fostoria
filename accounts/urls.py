"""Accounts app urls that are imported to main project urls"""
from django.urls import path
from .views import register_view

urlpatterns = [
    path('register/', register_view, name="register"),
]
