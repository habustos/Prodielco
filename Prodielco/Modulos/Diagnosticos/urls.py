from django.contrib import admin
from django.urls import path, include
#from django.urls import path, re_path
from django.conf.urls import  url
from django.contrib.auth.decorators import login_required
from app import views

urlpatterns = [
    #'',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
]