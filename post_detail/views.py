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

        # Only retrieves selected post if it has status: Published
        post = get_object_or_404(

            Post.objects.filter(status=1),
            slug=slug

        )

        # Retrieves top-level comment parents
        comments = post.comments.filter(

            approved=True,
            parent__isnull=True

        ).order_by("-created_on")

        # Sets liked to False
        # Then sets it to True if user.id exists in Post likes
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(

            request,
            'post_detail/post_detail.html',
            {
                'post': post,
                "comments": comments,
                "liked": liked,
                'comment_form': CommentForm(),
            },
        )
