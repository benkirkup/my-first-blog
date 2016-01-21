from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255, blank=False)
    abstract = models.CharField(max_length=400, blank=True, null=True)
    text = models.TextField(blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=False, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
