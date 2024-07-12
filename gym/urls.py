# src/gym/urls.py

# Module
from django.urls import path

from gym import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("why/", views.why_view, name="why"),
    path("trainer/", views.trainer_view, name="trainer"),
]
