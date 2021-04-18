from django.urls import path

from core.views import home_view

urlpatterns = [
    path("home/", home_view, name="home"),
]