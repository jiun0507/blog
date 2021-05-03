from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from notification.models import Notification
from valuation.models import Valuation
from . import forms


# Create your views here.
class LoginView(FormView):
    template_name = "user/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("core:home"))


class UserView(View):
    def get(self, request):
        user = request.user
        valuations = Valuation.objects.filter(user=user)
        notifications = Notification.objects.filter(user=user)

        context = {
            "notifications": notifications,
            "valuations": valuations,
            "user": user,
        }
        return render(request, "user/user.html", context=context)


class SignUpView(FormView):

    template_name = "user/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)