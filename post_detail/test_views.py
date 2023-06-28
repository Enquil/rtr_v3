from django.test import TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests


class TestPostDetailView(TestCase):

    # Test templates when getting the PostDetail view
    def test_get_post_detail_templates(self):

        category_model = Category.objects.create(
            friendly_name='General',
            name='general'
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
        post.likes.set(('1'))
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

    def test_add_like(self):
        category_model = Category.objects.create()
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
        post.likes.set((''))
        # Add a like test
        self.assertTrue(post.likes.count() == 0)
        post.likes.add(user)
        self.assertTrue(post.likes.count() == 1)
        # Template test
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertTrue(post.slug == 'how-to-crack-codes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

    def test_remove_likes(self):
        category_model = Category.objects.create()
        # Creates User object to be used as post author
        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )
        # Creates Post object
        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category_model,
            slug='how-to-crack-codes'
        )
        post.likes.set(('1'))
        # Remove a like test
        self.assertFalse(post.likes.count() == 0)
        post.likes.remove('1')
        self.assertTrue(post.likes.count() == 0)
        # Template test
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')
