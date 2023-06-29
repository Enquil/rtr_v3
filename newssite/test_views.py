from django.test import RequestFactory, TestCase
from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)


class TestPostList(TestCase):

    def test_get_post_list(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newssite/index.html', 'base.html')
