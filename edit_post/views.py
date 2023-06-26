from django.shortcuts import render
from create_post.forms import PostForm


class EditPost(View):

    def get(self, request, slug, *args, **kwargs):

        template = 'post_detail/post_detail.html'

        # Retrieves post based on slug, could be safer using id?
        post = get_object_or_404(
            Post.objects.filter(slug=slug),
        )
