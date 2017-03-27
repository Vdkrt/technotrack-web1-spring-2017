# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Blog, Post
from django import forms
from django.shortcuts import resolve_url


# Create your views here.

class SortBlogFrom(forms.Form):
    sort = forms.ChoiceField(
        choices=(
            ('title', u'Заголовок'),
            ('rate', u'Рейтинг'),
            ('description', u'Описание'),
            ('created_at', u'Дате публикации'),
        ),

    )

    search = forms.CharField(required=False)


class SortPostFrom(forms.Form):
    sort = forms.ChoiceField(
        choices=(
            ('title', u'Заголовок'),
            ('created_at', u'Дате публикации'),
        ),

    )

    search = forms.CharField(required=False)


class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = 'posts/blogs.html'

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortBlogFrom(request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            queryset = queryset.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                queryset = queryset.filter(title=self.sortform.cleaned_data['search'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortPostFrom(request.GET)
        return super(BlogView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(BlogView, self).get_queryset()
        if self.sortform.is_valid():
            queryset = queryset.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                queryset = queryset.filter(title=self.sortform.cleaned_data['search'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        return context


class PostView(DetailView):
    queryset = Post.objects.all()
    template_name = 'posts/post.html'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description')


class UpdateBlog(UpdateView):
    template_name = 'posts/editblog.html'
    model = Blog
    fields = ('title', 'description', 'category')

    def get_success_url(self):
        return resolve_url('blogs:oneblog', pk=self.object.id)


class CreateBlog(CreateView):
    template_name = 'posts/createblog.html'
    model = Blog
    fields = ('title', 'description', 'category')

    def get_success_url(self):
        return resolve_url('blogs:oneblog', pk=self.object.id)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class UpdatePost(UpdateView):
    template_name = 'posts/editpost.html'
    model = Post
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('blogs:onepost', pk=self.object.id)


class CreatePost(CreateView):
    template_name = 'posts/createpost.html'
    model = Post
    user = get_user_model()
    blog = forms.ChoiceField(queryset=Blog.objects.filter(author=user), label=u'Выберите блог')
    fields = ('title', 'text')

    def get_success_url(self):
        return resolve_url('blogs:onepost', pk=self.object.id)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreatePost, self).form_valid(form)
