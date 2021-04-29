from django.contrib import admin
from . import models


@admin.register(models.CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "ticker",
        "name",
        "locale",
        "active",
    )
