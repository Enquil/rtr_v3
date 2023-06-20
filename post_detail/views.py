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

        template = 'post_detail/post_detail.html'

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

            request, template,
            {
                'post': post,
                "comments": comments,
                "liked": liked,
                'comment_form': CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):

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

        comment_form = CommentForm(
            data=request.POST
        )

        if comment_form.is_valid():

            comment_form.instance.name = request.user.username
            parent_obj = None
            parent_id = None

            # get parent comment id from hidden input (if it exists)
            if request.POST.get('parent_id'):
                # Make sures the id is an int
                parent_id = int(request.POST.get('parent_id'))

            '''
            if parent_id exists in the form,
            stores the comment from the comments queryset,
            with corresponding id as parent_obj
            '''
            if parent_id:
                parent_obj = comments.get(id=parent_id)
                # if parent object exists
                if parent_obj:
                    # create reply comment object
                    reply_comment = comment_form.save(commit=False)
                    # assign parent_obj ID to reply comment as foreign key
                    reply_comment.parent = parent_obj

            # if NOT a reply comment
            # create comment object
            comment = comment_form.save(commit=False)
            # assign comment to post
            comment.post = post
            # save
            comment.save()
            messages.success(
                request, f'Your comment was succesfully posted'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

        else:
            comment_form = CommentForm()

        return render(
            request, template,
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug):

        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
