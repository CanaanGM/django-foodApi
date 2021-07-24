from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user model with an email is successful"""

        email = 'test@test.com'
        password = 'testApC12'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test the email of a new user is normilized"""
        email = 'test@TEST.com'
        password = 'testApC12'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test create a super user"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'timetofeast!'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)