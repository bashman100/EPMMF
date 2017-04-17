from django.contrib.auth.models import User
from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('assets/bioimg', str(instance.id), filename)

# Create your models here.
class band(models.Model):
    priority = models.CharField(max_length=2)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.URLField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name


class sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)


    def __str__(self):
        return self.name
