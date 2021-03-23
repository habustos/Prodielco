from django.contrib import admin
from django.urls import path, include
#from django.urls import path, re_path
from django.conf.urls import  url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    #'',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    #url(r'^add/$', views.Cliente, name='modele_new'),
    path('C_add/', views.add_buyer.as_view(template_name="pruebas/cliente.html"), name='cliente_add'),
    #path('r-aisl/', views.R_aisl_view.as_view(template_name="pruebas/R_aisl.html"), name='aisl'),
    url('r-aisl/', views.R_aisl_view, name='aisl'),
    #path('r-aisl/', views.R_aisl_view, name='r-aisl'),
]