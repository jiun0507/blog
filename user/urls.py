from django.urls import path
from user.views import (
    LoginView,
    LogoutView,
    RelationCreateView,
    RelationDeleteView,
    UserView,
    SignUpView,
)

app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/<int:id>", UserView.as_view(), name="profile"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("follow/<int:followee_id>", RelationCreateView.as_view(), name="follow"),
    path("unfollow/<int:followee_id>", RelationDeleteView.as_view(), name="unfollow"),
]
