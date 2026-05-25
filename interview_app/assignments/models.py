from django.db import models
from django.conf import settings


class Assignment(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignments"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
