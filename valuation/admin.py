from django.contrib import admin
from . import models


@admin.register(models.Valuation)
class ValuationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = ("id",)
