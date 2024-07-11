# src/convert_html/urls.py

# modul
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),

    # gym
    path("", include("gym.urls")),
]
