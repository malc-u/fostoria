"""Accounts app tests"""
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from .forms import UserRegistrationForm
from .views import register_view, logout_view, profile_view


# Testing user registration

class TestRegisterView(TestCase, Client):
    """
    Testing register_view
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_register_page(self):
        """
        Test checking if register_view is sucessfully loaded (status 200)
        when URL ("/accounts/register/") called.
        """
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
    
    def test_get_register_template(self):
        """
        Test checking if correct template is used ('register.html' and all
        others that were included on this template) when URL ("/accounts/register/") called.
        """
        response = self.client.get("/accounts/register/")
        self.assertTemplateUsed(response, 'register.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'includes/head.html')
        self.assertTemplateUsed(response, 'includes/header.html')
        self.assertTemplateUsed(response, 'includes/navbar-menu.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-mobile.html')
        self.assertTemplateUsed(response, 'includes/nav-buttons-desktop.html')
        self.assertTemplateUsed(response, 'includes/top-footer-sec.html')
        self.assertTemplateUsed(response, 'includes/footer.html')
        self.assertTemplateUsed(response, 'includes/scripts.html')
        self.assertTemplateNotUsed(response, 'contact.html')

class TestRegisterUrl(SimpleTestCase):
    """
    Testing Register Url
    """

    def test_register_url_is_resolved(self):
        """
        Test checking if reversed url 'register' resolved to
        'register_view' function
        """
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

class TestUserRegistrationForm(TestCase):
    """
    Testing User Registration Form
    """
    def test_cannot_create_new_user_with_just_username(self):
        """
        Confirming that more than 1 field (username in this case) is needed to create new user
        """
        form = UserRegistrationForm({'username': 'newuser'})
        self.assertFalse(form.is_valid())

# Logout Url test
def test_logout_url_is_resolved(self):
    """
    Test checking if reversed url 'logout' resolved to
        logout_view' function
    """
    url = reverse('logout')
    self.assertEqual(resolve(url).func, logout_view)

