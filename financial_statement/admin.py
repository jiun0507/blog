from django.contrib import admin
from . import models


@admin.register(models.FinancialStatement)
class FinancialStatementAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "ticker",
        "period",
        "calendar_date",
        "report_period",
        "assets",
    )

    list_filter = ("ticker",)
