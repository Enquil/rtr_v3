from django.test import TestCase
from .forms import CommentForm
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User


class TestCommentForm(TestCase):
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

    def test_body_is_required(self):
        '''
        Test if body is required (Empty Form)
        '''
        user = User.objects.get(id=1)

        form = CommentForm({'author': user, 'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
