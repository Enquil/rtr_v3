from django.urls import path
from . import views


urlpatterns = [
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
]
