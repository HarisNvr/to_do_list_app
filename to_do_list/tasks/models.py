from django.db import models
from django.contrib.auth.models import User

from tasks.constants import TITLE_LENGTH


class ToDo(models.Model):
    title = models.CharField(max_length=TITLE_LENGTH)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos'
    )

    def __str__(self):
        return self.title
