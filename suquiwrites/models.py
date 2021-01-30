from django.db import models
from django.conf import settings


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50, blank="False", default="guest")
    text = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    connected_entry = models.ForeignKey(
        Entry, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author + "," + self.connected_entry.title[:40]
