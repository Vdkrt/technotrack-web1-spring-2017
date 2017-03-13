from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Post

# Create your views here.
class BlogsList(ListView):

    queryset = Blog.objects.all()
    template_name = 'posts/blogs.html'

class BlogView(DetailView):

    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'

class PostView(DetailView):

    queryset = Post.objects.all()
    template_name = 'posts/post.html'

