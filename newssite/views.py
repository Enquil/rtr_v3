from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage


class PostList(View):
    '''
    - Sourced from Code Institute
    '''
    model = Post
    ordering = ['-created_on']
    template_name = "newssite/index.html"
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        post_list = Post.objects.all()
        paginator = Paginator(post_list, 2)

        return render(
            request, "newssite/index.html",
            {
                'post_list': post_list,
                'paginator': paginator
            }
        )
