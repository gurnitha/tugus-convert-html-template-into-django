# src/gym/urls.py

# Module
from django.urls import path

from gym import views

urlpatterns = [
    path("", views.home_view, name="home"),
]
