from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post

urlpatterns = [
    path(
        '',
        ListView.as_view(
            queryset=Post.objects.all().order_by("-date")[:25],
            template_name="blog/blog.html"  # full path to template
        ),
        name='blog_home'
    ),
    path(
        '<int:pk>/',
        DetailView.as_view(
            model=Post,
            template_name="blog/post.html"
        ),
        name='blog_detail'
    ),
]
# This file defines the URL patterns for the blog app in a Django project.