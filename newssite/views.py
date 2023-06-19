from django.shortcuts import render
from django.views import View, generic
from .models import Post
from django.contrib import messages


class PostList(generic.ListView):
    '''
    - Sourced from Code Institute
    '''
    model = Post
    ordering = ['-created_on']
    template_name = "newssite/index.html"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        print(kwargs)
        category = self.request.GET.get('category', None)
        print(category)
        return Post.objects.filter(status=1)
