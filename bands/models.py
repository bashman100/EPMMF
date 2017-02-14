from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class band(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    video = models.URLField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
