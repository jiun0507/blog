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
