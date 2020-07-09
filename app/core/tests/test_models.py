from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating user with email"""
        email = "test@test.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@TEST.COM"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email="")

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="admin@admin.com", password="admin")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
