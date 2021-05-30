from django.contrib import admin

from . import models


@admin.register(models.Post)
class Post(admin.ModelAdmin):

    """ User Admin Definition """

    list_display = (
        "id",
        "category",
        "title",
        "content",
    )
