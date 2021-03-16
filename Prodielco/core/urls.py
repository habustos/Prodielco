# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path("", include("app.urls")),
    path("", include("Modulos.Diagnosticos.urls"))
]
