from django.urls import path

from core.views import home_view

app_name = "core"

urlpatterns = [
    path("home/", home_view, name="home"),
]