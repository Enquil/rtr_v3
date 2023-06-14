from newssite.models import Post, Comment
from django.views import View
from .forms import CommentForm
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(

            approved=True,
            parent__isnull=True

        ).order_by("-created_on")

        template = 'post_detail/post_detail.html'

        return render(

            request,
            template,
            {
                'post': post,
                'comment_form': CommentForm(),
            },
        )
