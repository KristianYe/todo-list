from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime_created_at = models.DateTimeField(auto_now_add=True)
    datetime_deadline = models.DateTimeField()
    status = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")


class Tag(models.Model):
    name = models.CharField(max_length=255)
