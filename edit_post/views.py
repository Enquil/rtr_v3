from django.views import View
from django.shortcuts import render
from newssite.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
from create_post.forms import PostForm
from django.views.generic import UpdateView
from django.http import Http404
from django.core.exceptions import PermissionDenied


class EditPost(UpdateView):

    model = Post
    form_class = PostForm
    template_name = "edit_post/edit_post.html"
    success_url = "/profile/"

    def get_object(self, *args, **kwargs):
        post = super(EditPost, self).get_object(*args, **kwargs)
        if not post.author == self.request.user:
            raise PermissionDenied
        return post

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
