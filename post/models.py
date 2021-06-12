from django.db import models


class Post(models.Model):
    MEMO = "memo"
    ALGORITHM = "algorithm"
    DOTORI_POSTOFFICE = "dotori postoffice"
    WEDDEW = "weddew"
    POST_CHOICES = (
        (MEMO, "MEMO"),
        (ALGORITHM, "ALGORITHM"),
        (WEDDEW, "WEDDEW"),
        (DOTORI_POSTOFFICE, "DOTORI POSTOFFICE"),
    )
    title = models.CharField(max_length=100, blank=False)
    category = models.CharField(choices=POST_CHOICES, max_length=100, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Log(models.Model):
    date = models.DateField(auto_now=True)
    content = models.TextField(null=True)


class Work(models.Model):
    WORKOUT = "workout"
    ALGORITHM = "algorithm"
    SOFTWARE_DEVELOPMENT = "software development"
    READING = "reading"
    DOTORI_POSTOFFICE = "dotori postoffice"
    WEDDEW = "weddew"
    WORK_CATEGORIES = (
        (WORKOUT, "WORKOUT"),
        (ALGORITHM, "ALGORITHM"),
        (SOFTWARE_DEVELOPMENT, "SOFTWARE DEVELOPMENT"),
        (READING, "READING"),
        (DOTORI_POSTOFFICE, "DOTORI POSTOFFICE"),
        (WEDDEW, "WEDDEW"),
    )
    work_choices = models.CharField(
        choices=WORK_CATEGORIES, max_length=100, blank=False
    )
    hours = models.IntegerField(default=1)
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
