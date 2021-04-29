from django.contrib import admin
from notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    "Notification Admin Definition"
    list_display = (
        "company",
        "price",
        "active",
    )
