from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView


class CustomUserTests(TestCase):

    # test creation of a normal user
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="gabe",
            email="gabe@bookstore.com",
            password="testpass1234"
        )
        self.assertEqual(user.username, "gabe")
        self.assertEqual(user.email, "gabe@bookstore.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # test creation of a superuser
    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username="admin",
            email="admin@bookstore.com",
            password="testpass1234"
        )
        self.assertEqual(super_user.username, "admin")
        self.assertEqual(super_user.email, "admin@bookstore.com")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "users/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I want to be on the platform")


    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )