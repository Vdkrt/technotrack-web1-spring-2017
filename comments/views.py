# -*- coding: utf-8 -*-

from django import forms
from django.shortcuts import render, get_object_or_404, resolve_url
from django.views.generic import ListView, CreateView

from comments.models import Comment
from posts.models import Post

# Create your views here.

class SortCommentFrom(forms.Form):
    sort = forms.ChoiceField(
        choices=(
            ('text', u'Тексту'),
            ('create_date', u'Дате публикации'),
        ),
        required=False
    )

    search = forms.CharField(required=False)

class CommentsList(ListView):


    queryset = Post.objects.all()
    template_name = 'comments/comments.html'

class PostDetail(CreateView):
    model = Comment
    template_name = 'posts/post_and_comments.html'
    fields = ('text', )

    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortCommentFrom(request.GET)
        self.post = get_object_or_404(Post, id = kwargs['pk'])
        return super(PostDetail, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(PostDetail, self).get_queryset()
        if self.sortform.is_valid():
            if self.sortform.cleaned_data['sort']:
                queryset = queryset.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                queryset = queryset.filter(text=self.sortform.cleaned_data['search'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['sortform'] = self.sortform
        context['post'] = self.post
        return context

    def get_success_url(self):
        return resolve_url('blogs:onepost', pk = self.post.id)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(PostDetail, self).form_valid(form)

