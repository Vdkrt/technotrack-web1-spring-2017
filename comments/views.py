from django.shortcuts import render, get_object_or_404, resolve_url
from django.views.generic import ListView, CreateView

from comments.models import Comment
from posts.models import Post

# Create your views here.

class CommentsList(ListView):


    queryset = Post.objects.all()
    template_name = 'comments/comments.html'

class PostDetail(CreateView):
    model = Comment
    template_name = 'posts/post_and_comments.html'
    fields = ('text', )

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, id = self.kwargs['pk'])
        return context

    def get_success_url(self):
        return resolve_url('blogs:onepost', pk = self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        form.instance.post = get_object_or_404(Post, id = self.kwargs['pk'])
        return super(PostDetail, self).form_valid(form)