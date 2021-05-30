from django.db import models

# Create your models here.
class Post(models.Model):
    MEMO = "memo"
    ALGORITHM = "algorithm"
    LOG = "log"

    POST_CHOICES = ((MEMO, "MEMO"), (ALGORITHM, "ALGORITHM"), (LOG, "LOG"))
    content = models.TextField()
    category = models.CharField(choices=POST_CHOICES, max_length=15, blank=True)
    title = models.CharField(max_length=100, blank=False)