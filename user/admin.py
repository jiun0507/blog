from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "username",
        "email",
        "is_active",
    )
