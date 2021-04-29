from django.db import models
from company.models import CompanyModel
from user.models import User


class Notification(models.Model):

    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    price = models.FloatField()
    repeat = models.BooleanField()
    active = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
