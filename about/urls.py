""" About app urls to be imported to main project urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
]
