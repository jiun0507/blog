from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    writer = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
