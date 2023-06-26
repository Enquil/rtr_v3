from django.urls import path
from . import views


urlpatterns = [
    path('', views.EditPost.as_view(), name='edit_post'),
]
