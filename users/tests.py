from django.contrib.auth import get_user_model
from django.test import TestCase


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
