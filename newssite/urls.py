from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="index"),
    path('<str:category>', views.PostList.as_view(), name="index"),
]
