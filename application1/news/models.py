from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from blog.models import Blog


class Article (models.Model):

    post = models.ForeignKey(Blog)

    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)