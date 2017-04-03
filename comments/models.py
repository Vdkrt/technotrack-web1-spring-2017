from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from posts.models import Post


# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments')
    likes = models.IntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)