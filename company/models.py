from django.db import models


class CompanyModel(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    market = models.CharField(max_length=10)
    locale = models.CharField(max_length=10)
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.ticker + "(" + self.name + ")"