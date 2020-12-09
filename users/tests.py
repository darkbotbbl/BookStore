from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve


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

    username = "testuser"
    email = "testuser@site.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "I want to be on the platform")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
