from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    """ User Admin Definition """

    list_display = (
        "id",
        "username",
        "email",
        "is_active",
    )


@admin.register(models.FollowRelation)
class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ("follower",)
