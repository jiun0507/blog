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


class WorkInline(admin.TabularInline):
    model = models.Work


@admin.register(models.Log)
class Log(admin.ModelAdmin):

    """ User Admin Definition """

    list_display = (
        "date",
        "content",
    )
    inlines = (WorkInline,)
