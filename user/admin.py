from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    """ User Admin Definition """

    list_display = (
        "username",
        "email",
        "is_active",
    )
