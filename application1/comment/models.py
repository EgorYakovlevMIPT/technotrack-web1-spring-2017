from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from news.models import Article


class Remark (models.Model):

    post = models.ForeignKey (Article)

    #author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    pub_Date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)