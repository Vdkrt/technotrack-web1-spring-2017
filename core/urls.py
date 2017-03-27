# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from .views import RegisterFormView


urlpatterns = [

    url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
    url(r'^logout/', logout, {'template_name': 'core/logout.html'}, name="logout"),
    url(r'^register/', RegisterFormView.as_view(), {'template_name': 'core/register.html'}, name="register"),

]




