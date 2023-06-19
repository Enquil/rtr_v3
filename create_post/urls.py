from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreatePost.as_view(), name='create_post'),
]
