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
from django.contrib.messages.views import SuccessMessageMixin


class EditPost(SuccessMessageMixin, UpdateView):

    model = Post
    form_class = PostForm
    template_name = "edit_post/edit_post.html"
    success_url = "/profile/"
    success_message = 'Post was successfully Updated!'

    def get_object(self, *args, **kwargs):
        post = super(EditPost, self).get_object(*args, **kwargs)
        # Checks if logged in user is same as the posts author
        # if not, renders a 405 response
        if not post.author == self.request.user:
            return render(request, "error_pages/405.html", status=405)
        return post

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(self.POST)
        return super().form_valid(form)
