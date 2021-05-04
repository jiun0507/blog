from django.db import models


class CompanyModel(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    market = models.CharField(max_length=10)
    locale = models.CharField(max_length=10)
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.ticker + " : " + self.name
