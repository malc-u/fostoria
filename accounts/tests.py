"""Accounts app tests"""
from django.test import Client, RequestFactory, TestCase, SimpleTestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .forms import UserRegistrationForm, UserUpdateForm
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

# Testing user profile
class TestProfileViewUserNotLoggedIn(TestCase, Client):
    """
    Testing profile_view
    """

    def setUp(self):
        """
        Create client to conduct unit tests.
        """
        self.client = Client()

    def test_get_profile_page(self):
        """
        Test checking if profile_view is sucessfully loaded (status 200)
        when URL ("/accounts/profile/") called.
        """
        response = self.client.get("/accounts/profile/")
        self.assertEqual(response.status_code, 302)

class TestProfileViewUserLoggedIn(TestCase):
    """Testing profile_view for logged in user"""
    def setUp(self):
        """
        Accessing the request factory and creating user for testing.
        """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='test@email.com', password="testpassword1"
        )

    def test_user_update_form_exists_in_profile_view_context(self):
        client = Client()
        client.login(username='testuser', password="testpassword1")

        response = client.get('/accounts/profile/')
        form = response.context['form']
        form_type = type(form)
        self.assertEqual(form_type, UserUpdateForm)
