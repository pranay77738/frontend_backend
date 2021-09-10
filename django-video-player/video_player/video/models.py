from django.db import models
from django.utils import timezone


class History(models.Model):
    history_url = models.URLField(unique=True)
    date_watched = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.history_url


class Bookmark(models.Model):
    bookmark_url = models.URLField(unique=True)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bookmark_url
