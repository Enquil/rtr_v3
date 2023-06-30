from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileTest(TestCase):

    def setUp(self):

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

    def test_user_profile_str_method(self):
        '''
        Test UserProfile __str__ method
        '''
        user = User.objects.get(id=1)
        user_profile = UserProfile.objects.get(id=1)

        self.assertEqual(user.username, str(user_profile))

    def test_user_profile_exists(self):
        '''
        Tests if UserProfile is created when User is
        '''
        user = User.objects.create(
            username='ada',
            is_superuser=False,
            password='difference'
        )

        user_profile = UserProfile.objects.get(id=2)

        self.assertTrue(user_profile)
        # Test that the correct UserProfile actually shows up
        self.assertEqual(user_profile.user.username, 'ada')
