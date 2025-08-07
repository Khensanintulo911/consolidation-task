from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),  # home page
    path('projects/', views.projects, name='projects'),
    path('tech-stack/', views.tech_stack, name='tech_stack'),
]
# This file defines the URL patterns for the personal app in a Django project.
