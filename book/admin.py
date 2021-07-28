from django.contrib import admin

from . import models


@admin.register(models.Book)
class Book(admin.ModelAdmin):

    """ User Admin Definition """

    list_display = (
        "id",
        "title",
        "writer",
        "content",
        "created_at",
    )
