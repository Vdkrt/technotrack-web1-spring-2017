from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

class Blog(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    blog = models.ForeignKey(Blog)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='like')
    post = models.ForeignKey(Post)
