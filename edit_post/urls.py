from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
handler404 = "edit_post.views.custom_404"

urlpatterns = [
    path(
        '<slug:slug>',
        login_required(views.EditPost.as_view()),
        name='edit_post'
        ),
]
