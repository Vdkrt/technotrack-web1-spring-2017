from django.conf.urls import url
from .views import CommentsList, PostDetail

urlpatterns = [

    url(r'^$', CommentsList.as_view(), name='allblogs'),
#   url(r'^$', PostDetail.as_view(), name='onepost'),

]