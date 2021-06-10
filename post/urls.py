from django.urls import path
from post.views import (
    PostView,
)

app_name = "post"

urlpatterns = [
    path("<int:id>", PostView.as_view(), name="get"),
    path("list", PostView.as_view(), name="list"),
]
