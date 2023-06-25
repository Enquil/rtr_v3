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
    # Sets number of items to be displayed per page
    paginate_by = 2
    filtered = False

    def get_queryset(self):
        '''
        Overrides default behavior when getting the queryset
        Lets user filter by category
        '''
        category = self.request.GET.get('category')
        if category is not None:
            filtered = True
            return Post.objects.filter(
                category=category).order_by('-created_on')
        else:
            return Post.objects.all().order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.request.GET.get('category')
        print(context)
        return context

    def urlencode_filter(self):
        qd = self.request.GET.copy()
        print(qd)
        qd.pop(self.page_kwarg, None)
        return qd.urlencode()
