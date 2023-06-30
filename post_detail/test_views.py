from django.test import RequestFactory, TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests
from .views import PostDetail, PostLike


class TestPostDetailView(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

        category = Category.objects.create(
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
            password='difference',
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category,
        )

        comment = Comment.objects.create(
            post=post,
            author=user2,
            body='Great job Alan!'
        )

        comment2 = Comment.objects.create(
            post=post,
            parent=comment,
            author=user,
            body='This looks amazing!'
        )

    def test_get_post_detail(self):
        '''
        Tests statuscode of PostDetailView
        and that correct template is being used
        when rendering post_detail view
        '''

        post = Post.objects.get(id=1)

        response = self.client.get(reverse('post_detail', args=(post.slug,)))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

    def test_get_post_detail_add_comment(self):
        '''
        Tests if only top-level comments are retrieved
        '''
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        response = self.client.post(reverse('post_detail', args=(post.slug,)))


class TestPostComment(TestCase):

    def setUp(self):

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma',
        )

        post = Post.objects.create(
            title="Test post", author=user, slug="test",
            excerpt="Test excerpt", content="Test content", status=1
        )

    def test_comment(self):
        user = User.objects.get(id=1)
        self.client.force_login(User.objects.get(id=1))
        post = Post.objects.get(id=1)
        response = self.client.post(reverse('post_detail', args=[post.slug]), {
            'author': user,
            'post': post,
            'body': 'This is a test comment'
        })
        comment.save()
        print(post.comments)
