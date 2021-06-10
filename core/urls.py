from django.urls import path

from core.views import home_view, landing_page_view, out_of_service

# This must be same as the namespace in the config.urls.py
# This allows this view to be used as a url tag in the html.
app_name = "core"

urlpatterns = [
    path("", home_view, name="home"),
    path("land", landing_page_view, name="landing_page"),
    path("out_of_service/<str:service>", out_of_service, name="out_of_service"),
]