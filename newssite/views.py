from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage


class PostList(ListView):
    '''
    Sourced from Code Institute
    '''
    model = Post
    ordering = ['-created_on']
    template_name = "newssite/index.html"
    # Sets number of items to be displayed per page
    paginate_by = 3

    def get_queryset(self):
        '''
        Overrides default behavior when getting the queryset
        Lets user filter by category
        '''
        category = self.request.GET.get('category')
        if category is not None:
            return Post.objects.filter(
                category=category).order_by('-created_on')
        return Post.objects.all().order_by('-created_on')
