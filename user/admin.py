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


from user.models import FollowRelation


class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ("follower",)
