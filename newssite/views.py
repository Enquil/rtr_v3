from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.utils.http import urlencode


class PostList(ListView):
    '''
    Sourced from Code Institute
    '''
    model = Post
    ordering = ['-created_on']
    template_name = "newssite/index.html"
    # number of items to be displayed per page
    paginate_by = 2

    def get_queryset(self):
        '''
        Overrides default behavior when getting the queryset
        '''

        # capture value passed for category
        category = self.request.GET.get('category')

        # filters by category if category is not None
        if category is not None:
            return Post.objects.filter(
                    category=category
                   ).order_by('-created_on')
        # just get all posts if category is None
        else:
            return Post.objects.all().order_by('-created_on')

    def get_context_data(self, **kwargs):
        '''
        Overrides default context behavior
        sets context['category'] to either:
        the category captured in request.GET OR None
        '''
        context = super().get_context_data(**kwargs)
        context["category"] = self.request.GET.get('category', None)
        return context
