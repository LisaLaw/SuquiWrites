from django.db import models
from django.conf import settings


class Entry(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Entries", blank=True, null=True)
    quote = models.TextField(max_length=200, default="", blank=True)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ["-published_date",]

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50, blank="False", default="guest")
    thoughts = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    connected_entry = models.ForeignKey(
        Entry, related_name="comments", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.name + "," + self.connected_entry.title[:40]
