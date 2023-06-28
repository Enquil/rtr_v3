from django.test import TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User


class CategoryModelTest(TestCase):

    def setUp(self):
        category_model = Category.objects.create(
            friendly_name='General',
        )
        category_model = Category.objects.create(
            friendly_name='Art and Entertainment',
        )

    def test_category_names(self):
        category_a = Category.objects.get(friendly_name='General')
        category_b = Category.objects.get(
            friendly_name='Art and Entertainment'
        )
        self.assertEqual(category_a.name, 'general')
        self.assertEqual(category_b.name, 'art_entertainment')


class PostModelTest(TestCase):

    def setUp(self):

        category_model = Category.objects.create(
            friendly_name='General',
        )

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category_model,
            slug='how-to-crack-codes'
        )

    def test_post_user(self):
        test_post = Post.objects.get(id=1)
        self.assertEqual(test_post.author.username, 'alan')
        self.assertEqual(test_post.slug)
