from newssite.models import Post, Comment
from django.views import View
from .forms import CommentForm
from django.shortcuts import (
    render, get_object_or_404,
    redirect, reverse
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):

        template = 'post_detail/post_detail.html'

        # Only retrieves selected post if it has status: Published
        post = get_object_or_404(
            Post.objects.filter(status=1),
            slug=slug
        )

        # Retrieves top-level comments, i.e no parents, like batman
        comments = post.comments.filter(
            approved=True,
            parent__isnull=True
        ).order_by("-created_on")

        # Sets liked to False
        liked = False
        # Sets liked to True if user.id exists in Post likes, in database
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(

            request, template,
            {
                'post': post,
                "comments": comments,
                "liked": liked,
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):

        template = 'post_detail/post_detail.html'

        # Only retrieves selected post if it has status: Published
        post = get_object_or_404(
                Post.objects.filter(status=1),
                slug=slug
        )

        # Retrieves top-level comments, i.e no parents, like batman
        comments = post.comments.filter(
            approved=True,
            parent__isnull=True
        ).order_by("-created_on")

        # Sets liked to False
        liked = False
        # Sets liked to True if user.id exists in Post likes, in database
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        if request.user.is_anonymous is False:

            comment_form = CommentForm(
                data=request.POST
            )

            if comment_form.is_valid():

                comment_form.instance.author = request.user.username
                parent_obj = None
                parent_id = None

                # get parent comment id from hidden input (if it exists)
                if request.POST.get('parent_id'):
                    # turn parent-id to an int to find the comment in comments
                    parent_id = int(request.POST.get('parent_id'))

                '''
                if parent_id exists in the form,
                stores the comment with the captured id as parent_obj
                '''
                if parent_id:
                    parent_obj = comments.get(id=parent_id)
                    # if parent object (comment) exists in database
                    if parent_obj:
                        # create reply comment object
                        reply_comment = comment_form.save(commit=False)
                        # assign parent_obj ID to reply comment as foreign key
                        reply_comment.parent = parent_obj

                # If not a reply, just create a comment object
                comment = comment_form.save(commit=False)
                # assign comment to post
                comment.post = post
                # save
                comment.save()
                messages.success(
                    request, f'Your comment was succesfully posted'
                )
                return HttpResponseRedirect(
                    reverse('post_detail', args=[slug])
                )
            else:
                comment_form = CommentForm()
        else:
            messages.error(request, f'Only logged in members can do that')

        return render(
            request, template,
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )


class PostLike(View):

    def post(self, request, slug):

        if request.user.is_anonymous is False:
            post = get_object_or_404(Post, slug=slug)

            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
        else:
            messages.error(request, f'Only logged in members can do that')

        return HttpResponseRedirect(
            reverse('post_detail', args=[slug])
        )
