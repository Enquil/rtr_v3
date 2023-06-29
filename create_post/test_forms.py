from django.test import TestCase
from .forms import PostForm
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User


class TestPostForm(TestCase):
    '''
    Sourced From CodeInstitute
    (whole class)
    Tests the CommentForm
    '''
    def setUp(self):

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        category = Category.objects.create(
            friendly_name='Ships and Giggles'
        )

    def test_title_is_required(self):
        '''
        Test if PostForm['title'] is required
        '''

        form = PostForm({'title': '', })

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_category_is_required(self):
        '''
        Test if PostForm['category'] is required
        '''

        form = PostForm({'category': '', })

        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')
