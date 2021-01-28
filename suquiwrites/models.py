from django.db import models
from django.conf import settings
from datetime import datetime


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self, value):
        self.published_date = datetime.strptime(value, "%d-%m-%Y").date()
        self.save()

    def __str__(self):
        return self.title