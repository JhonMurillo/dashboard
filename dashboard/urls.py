#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'dashboard'

urlpatterns = [
    # Retrieve task list
    path('', views.inicio, name='dashboard'),
]