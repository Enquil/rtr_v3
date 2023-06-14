from django.shortcuts import render
from django.views import View
from django.views import generic
from .models import Post
from django.contrib import messages


class PostList(generic.ListView):
    '''
    - Sourced from Code Institute
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "newssite/index.html"
    paginate_by = 5
