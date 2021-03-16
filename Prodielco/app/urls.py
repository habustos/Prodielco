# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from django.conf.urls import  url
from django.contrib.auth.decorators import login_required
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
