from django.test import RequestFactory, TestCase
from newssite.models import Post, Comment, Category
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
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

    def test_get_post_detail_logged_in(self):
        '''
        Tests statuscode of CreatePost View
        and that correct template is being used
        when rendering CreatePost View
        '''
        response = self.client.get('/create_post/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post/create_post.html')
