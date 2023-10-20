from django.db import models
from django.conf import settings


class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    # deadline =
    createdAt = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
# Create your models here.
