from newssite.models import Post, Comment
from django.views import View
from django.shortcuts import (
    render, get_object_or_404,
    redirect, reverse
)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import UserProfile


class ProfileView(View):

    def get(self, request, *args, **kwargs):

        if request.user.is_anonymous is False:
            profile = get_object_or_404(UserProfile, user=request.user)
            return render(
                request,
                "profiles/profile.html",
                {
                    'profile': profile,
                },
            )
        else:
            messages.error(
                request, f'You do not have permission for that'
            )
            return render(
                request,
                "newssite/index.html",
            )
