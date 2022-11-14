#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'reto'

urlpatterns = [
    # Retrieve task list
    path('', views.ListaPersona.as_view(), name='lista_personas'),
]