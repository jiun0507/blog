from django.urls import path
from post.views import (
    LogView,
    PostView,
)

app_name = "post"

urlpatterns = [
    path("<int:id>", PostView.as_view(), name="get"),
    path("list", PostView.as_view(), name="list"),
    path("logs", LogView.as_view(), name="logs"),
]
