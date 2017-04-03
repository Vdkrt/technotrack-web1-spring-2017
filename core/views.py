from django.shortcuts import render
from django.views.generic.base import TemplateView
from comments.models import Comment
from posts.models import Post, Blog
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url

# Create your views here.

class ShowError(TemplateView):
    template_name = 'core/error.html'

class CreateUser(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

class HomePageView(TemplateView):

    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_blogs'] = Blog.objects.count()
        context['latest_posts'] = Post.objects.count()
        context['latest_comments'] = Comment.objects.count()
        return context


class RegisterFormView(FormView):

    form_class = CreateUser
    template_name = 'core/register.html'

    def get_success_url(self):
        return resolve_url('core:login')

    def form_valid(self, form):

        form.save()
        return super(RegisterFormView, self).form_valid(form)

