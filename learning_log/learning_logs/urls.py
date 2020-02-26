"""Defines URL patterns for learning_logs."""

from django.urls import path, include

from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),

    # Show all topics.
    path(r'topics/', views.topics, name='topics'),
]