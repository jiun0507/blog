from django.db import models
from user.models import User


class ValuationCategory(models.Model):
    name = models.CharField(max_length=200)


class Valuation(models.Model):
    """Review Model Definition"""

    review = models.TextField()
    method = models.ForeignKey(ValuationCategory, on_delete=models.CASCADE)
    value = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
