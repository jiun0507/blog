from django.db import models


# Create your models here.
class Post(models.Model):
    MEMO = "memo"
    ALGORITHM = "algorithm"
    LOG = "log"

    POST_CHOICES = ((MEMO, "MEMO"), (ALGORITHM, "ALGORITHM"), (LOG, "LOG"))
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(choices=POST_CHOICES, max_length=15, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)