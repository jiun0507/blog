from django.urls import path
from user.views import LoginView, LogoutView, UserView, SignUpView

app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", UserView.as_view(), name="profile"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
