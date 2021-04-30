from django.urls import path
from notification.views import NotificationFormView, NotificationView

app_name = "notification"

urlpatterns = [
    path("form/", NotificationFormView.as_view(), name="form"),
    path("user/", NotificationView.as_view(), name="user"),
]
