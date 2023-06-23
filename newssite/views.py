from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage


class PostList(ListView):
    '''
    - Sourced from Code Institute
    '''
    model = Post
    ordering = ['-created_on']
    template_name = "newssite/index.html"
    paginate_by = 3

    def get_queryset(self):
        category = self.request.GET.get('category')
        return Post.objects.filter(category=category)
