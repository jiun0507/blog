from django.urls import path
from post.views import (
    PostView,
)

app_name = "user"

urlpatterns = [
    path("<int:id>", PostView.as_view(), name="get"),
]
