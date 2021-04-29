from django.db import models
from user.models import User


class ValuationCategory(models.Model):
    name = models.CharField(max_length=200)


class Valuation(models.Model):
    """Review Model Definition"""

    DCF = "dcf"
    REPRODUCTIOIN_COST = "reproduction_cst"
    OTHER = "other"
    METHOD_CHOICES = (
        (DCF, "DCF"),
        (REPRODUCTIOIN_COST, "Reproduction_cost"),
        (OTHER, "Other"),
    )
    ticker = models.CharField(max_length=10, null=True)
    review = models.TextField()
    method = models.CharField(choices=METHOD_CHOICES, max_length=20, blank=True)
    value = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
