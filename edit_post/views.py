from django.views import View
from django.shortcuts import (
    render, get_object_or_404,
    redirect, reverse
)
from newssite.models import Post
from create_post.forms import PostForm


class EditPost(View):

    def get(self, request, *args, **kwargs):

        template = 'edit_post/edit_post.html'
        slug = self.request.GET.get('slug')

        # Retrieves post based on slug, could be safer using id?
        post = get_object_or_404(
            Post.objects.filter(slug=slug),
        )

        return render(
            request,
            template,
            {
                "post": post,
                "post_form": PostForm(instance=post)
            },
        )
