from django.test import RequestFactory, TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect,
                         HttpRequest)
import requests
from .views import CreatePost


class TestCreatePostView(TestCase):

    def setUp(self):

        self.factory = RequestFactory()

        user = User.objects.create(
            username='alan',
            is_superuser=True,
            password='enigma'
        )

    def test_get_create_post_logged_in(self):
        '''
        With Logged in User:
        Tests statuscode of CreatePost View
        and that correct template is being used
        when rendering CreatePost View
        '''

        response = self.client.get('/create_post/')
        # Logged in User
        self.client.force_login(User.objects.get(id=1))
        response = self.client.get('/create_post/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post/create_post.html')

    def test_get_create_post_not_logged_in(self):
        '''
        Tests statuscode of CreatePost View when not logged in
        (Anonymous User)
        Tests that correct template is being used
        when rendering CreatePost View
        '''

        response = self.client.get('/create_post/')

        '''
        Tests for redirect 302 (found) and the template it should redirect to
        Template should be login + loginrequired() args
        '''
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            '/accounts/login/?next=/create_post/'
        )

    # def test_post_create_post(self):

    #     request = HttpRequest()
    #     self.client.force_login(User.objects.get(id=1))
    #     data = {'csrfmiddlewaretoken': ['bspcgV3YfFtSwpkXv253ZyFBTdvjYYhvnOpxAndgpasWiKggLFNZFillvwV6Jq4T'], "title": ["test_post"], "category": ["1"], "excerpt": [""], "content": ["Ipsum Lorem"]}
    #     response = self.client.post(
    #         '/create_post/',
    #         data=data,
    #     )

    #     self.assertTrue(form.is_valid())
