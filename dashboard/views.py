from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Persona, CalidadVida

from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView


# Create your views here.

def inicio(request):
    labels, saludLabel, movilidadLabel, viviendaLabel, estudioLabel = [], [], [], [], []
    data, saludData , movilidadData, viviendaData, estudioData = [], [], [], [], []

    querysetMuertes = CalidadVida.objects.values().filter(categoria='Muertes')
    for entry in querysetMuertes:

        data.append(entry['cantidad'])
        labels.append(entry['sub_categoria'])

    querysetSalud = CalidadVida.objects.values().filter(categoria='Salud')
    for entry in querysetSalud:

        saludData.append(entry['cantidad'])
        saludLabel.append(entry['sub_categoria']) 

    querysetVivienda = CalidadVida.objects.values().filter(categoria='Vivienda')
    for entry in querysetVivienda:

        viviendaData.append(entry['cantidad'])
        viviendaLabel.append(entry['sub_categoria']) 

    querysetMovilidad = CalidadVida.objects.values().filter(categoria='Movilidad')
    for entry in querysetMovilidad:

        movilidadData.append(entry['cantidad'])
        movilidadLabel.append(entry['sub_categoria'])  

    querysetEstudio = CalidadVida.objects.values().filter(categoria='Estudio')
    for entry in querysetEstudio:

        estudioData.append(entry['cantidad'])
        estudioLabel.append(entry['sub_categoria'])  


    return render(request, "dashboard/inicio.html", {
        'labels': labels,
        'data': data,
        'saludData': saludData,
        'saludLabel': saludLabel,
        'viviendaLabel': viviendaLabel,
        'viviendaData': viviendaData,
        'movilidadLabel': movilidadLabel,
        'movilidadData': movilidadData,
        'estudioLabel': estudioLabel,
        'estudioData': estudioData,
    })

class ListaPersona(ListView):
    model = Persona
    # context_object_name = 'persona'