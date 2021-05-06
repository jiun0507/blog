from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView

from notification.models import Notification
from user.models import FollowRelation, User
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
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404
        valuations = Valuation.objects.filter(user=user)
        notifications = Notification.objects.filter(user=user)
        if FollowRelation.objects.filter(follower=request.user, followee=user).exists():
            following = True
        else:
            following = False
        context = {
            "notifications": notifications,
            "valuations": valuations,
            "user": user,
            "following": following,
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


class RelationCreateView(View):
    def get(self, request, followee_id):
        try:
            relation = FollowRelation.objects.get(follower=request.user)
        except FollowRelation.DoesNotExist:
            relation = FollowRelation.objects.create(follower=request.user)

        try:
            if followee_id == request.user.id:
                raise IntegrityError
            relation.followee.add(followee_id)
            relation.save()
        except IntegrityError:
            return HttpResponse("Can't subscribe yourself")
        return redirect(reverse("core:home"))


class RelationDeleteView(View):
    def get(self, request, followee_id):
        try:
            relation = FollowRelation.objects.get(follower=request.user)
        except FollowRelation.DoesNotExist:
            return HttpResponse("Not following")
        try:
            if followee_id == request.user.id:
                raise IntegrityError
            relation.followee.remove(followee_id)
            relation.save()
        except IntegrityError:
            return HttpResponse("Can't subscribe yourself")
        except Exception as err:
            return HttpResponse(
                "Unidentified error when deleting a followee in FollowRelation instance."
            )

        return redirect(reverse("core:home"))