from django.shortcuts import render
from django.views import View

from notification.models import Notification
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
