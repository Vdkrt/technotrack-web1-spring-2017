from django.conf.urls import url, include
from .views import BlogsList, BlogView, PostView, UpdateBlog, UpdatePost, CreatePost, CreateBlog
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^blogs/(?P<pk>\d+)/$', BlogView.as_view(), name='oneblog'),
    url(r'^blogs/(?P<pk>\d+)/edit/$', login_required(UpdateBlog.as_view()), name='editblog'),
    url(r'^blogs/new/$', login_required(CreateBlog.as_view()), name='createblog'),
    url(r'^blogs/$', BlogsList.as_view(), name='allblogs'),
    url(r'^blogs/post/(?P<pk>\d+)/$', PostView.as_view(), name='onepost'),
    url(r'^blogs/post/new/$', login_required(CreatePost.as_view()), name='createpost'),
    url(r'^blogs/post/(?P<pk>\d+)/edit/$', login_required(UpdatePost.as_view()), name='editpost'),



]