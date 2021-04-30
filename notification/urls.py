from django.urls import path
from notification.views import NotificationFormView, NotificationView

app_name = "notification"

urlpatterns = [
    path("user/", NotificationFormView.as_view(), name="user"),
    path("update/", NotificationView.as_view(), name="update"),
]
