from django.shortcuts import render
from django.views.generic.base import TemplateView

from posts.models import Post, Blog

# Create your views here.

def test(request, post_id=None, comment_id=None, blog_id=None):
    return render(request, 'core/file.html', {"post_id": post_id, "blog_id": blog_id})



class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Blog.objects.all()[:5]
        return context