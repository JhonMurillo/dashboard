from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Persona

from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView


# Create your views here.

class ListaPersona(ListView):
    model = Persona
    # context_object_name = 'persona'