from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post

# Create your views here.

class CommentsList(ListView):


    queryset = Post.objects.all()
    template_name = 'comments/comments.html'

