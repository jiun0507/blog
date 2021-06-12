from django.urls import path
from post.views import (
    LogView,
    PostView,
    list_post,
)

app_name = "post"

urlpatterns = [
    path("<int:post_id>", PostView.as_view(), name="get"),
    path("list", list_post, name="list"),
    path("logs", LogView.as_view(), name="logs"),
]
