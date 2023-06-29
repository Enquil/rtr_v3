from django.test import RequestFactory, TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests
from .views import EditPost


class TestEditPostView(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

        category = Category.objects.create(
            friendly_name='Ships and Giggles',
        )

        post = Post.objects.create(
            title='how to crack codes',
            author=user,
            content="so easy",
            category=category,
        )

    def test_get_edit_post_logged_in(self):
        '''
        Tests statuscode of EditPost View with logged in user
        Tests that correct template is being used
        when rendering EditPost View
        '''
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get(f'/edit_post/{post.slug}')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_post/edit_post.html')

    def test_get_edit_post_not_logged_in(self):
        '''
        Tests statuscode of EditPost View when not logged in
        (Anonymous User)
        Tests that correct template is being used
        when rendering EditPost View
        '''
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)
        response = self.client.get(f'/edit_post/{post.slug}')

        # Tests for redirect 302 and the template it should redirect to
        # Template should be login + loginrequired() args
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=/edit_post/how-to-crack-codes-alan1'
        )
