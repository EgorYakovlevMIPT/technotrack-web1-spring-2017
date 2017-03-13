from __future__ import unicode_literals
from django.db import models

class Profile (models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()