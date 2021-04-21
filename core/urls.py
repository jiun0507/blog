from django.urls import path

from core.views import home_view

# This must be same as the namespace in the config.urls.py
# This allows this view to be used as a url tag in the html.
app_name = "core"

urlpatterns = [
    path("home/", home_view, name="home"),
]