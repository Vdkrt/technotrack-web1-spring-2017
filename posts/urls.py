from django.conf.urls import url, include
from .views import BlogsList, BlogView, PostView

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name='oneblog'),
    url(r'^$', BlogsList.as_view(), name='allblogs'),
    url(r'^(?P<pk>\d+)/post/(?P<post_id>\d+)/comments/', include('comments.urls', namespace='allcomment')),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='onepost'),


]