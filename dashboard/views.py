from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Persona, CalidadVida

from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView


# Create your views here.

def inicio(request):
    labels, saludLabel = [], []
    data, saludData = [], []

    querysetMuertes = CalidadVida.objects.values().filter(categoria='Muertes')
    for entry in querysetMuertes:

        data.append(entry['cantidad'])
        labels.append(entry['sub_categoria'])

    querysetSalud = CalidadVida.objects.values().filter(categoria='Salud')
    for entry in querysetSalud:

        saludData.append(entry['cantidad'])
        saludLabel.append(entry['sub_categoria'])
    


    return render(request, "dashboard/inicio.html", {
        'labels': labels,
        'data': data,
        'saludData': saludData,
        'saludLabel': saludLabel,
    })

class ListaPersona(ListView):
    model = Persona
    # context_object_name = 'persona'