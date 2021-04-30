from notification.models import Notification
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views import View
from notification.use_case.add_notification import NotificationUseCase
from . import forms


class NotificationFormView(FormView):
    template_name = "notification/add_notification.html"
    form_class = forms.NotificationForm
    success_url = reverse_lazy("notification:user")


class NotificationView(View):
    def __init__(self):
        self.notification_update_use_case = NotificationUseCase()

    def post(self, request):
        form = forms.NotificationForm(request.POST)
        if form.is_valid():
            user = request.user
            self.notification_update_use_case.add_notification(
                company=form.cleaned_data["company"],
                price=form.cleaned_data["price"],
                repeat=form.cleaned_data["repeat"],
                active=form.cleaned_data["active"],
                user=user,
            )

        return HttpResponse("successfully posted")