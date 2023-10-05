from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime_created_at = models.DateTimeField(auto_now_add=True)
    datetime_deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["is_done", "-datetime_created_at"]

    def __str__(self):
        return f"{self.content}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"