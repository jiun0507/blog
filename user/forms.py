from django import forms
from . import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = models.User.objects.get(username=username)
            if not user.check_password(password):
                self.add_error("password", forms.ValidationError("password is wrong"))
        except models.User.DoesNotExist:
            raise self.add_error("username", forms.ValidationError("user does not exist"))

        return self.cleaned_data