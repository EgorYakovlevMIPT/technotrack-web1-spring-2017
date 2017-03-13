from __future__ import unicode_literals
from django.db import models
from MyModle.models import Profile

class Blog (models.Model):

    post = models.ForeignKey(Profile)
    title = models.CharField(max_length=255)
