from django.conf.urls import url
from .views import CommentsList

urlpatterns = [

    url(r'^$', CommentsList.as_view(), name='allblogs'),

]