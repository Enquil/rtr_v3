from django.test import RequestFactory, TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests


class TestPostDetailView(TestCase):

    def setUp(self):

        category_model = Category.objects.create(
            friendly_name='General',
        )

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        user2 = User.objects.create(
            username='ada',
            is_superuser=False,
            password='difference'
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category_model,
        )

        post2 = Post.objects.create(
            title='Calculating machines',
            author=user2,
            content="sometimes, 1 is 0",
            category=category_model,
        )

    # Test templates when getting the PostDetail view
    def test_get_post_detail_template(self):

        category_model = Category.objects.get(id=1)
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        post.likes.set(('1'))
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')
