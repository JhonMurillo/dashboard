from django.db import models
from django.contrib import admin

# Create your models here.

class NivelEstres(models.TextChoices):
    ALTO = 'a', "Alto"
    BAJO = 'b', "Bajo"
    NORMAL = 'n', "Normal"


class Persona(models.Model):
    nombre = models.CharField(max_length = 200)
    apellido = models.CharField(max_length = 200)
    edad = models.CharField(max_length = 200)
    peso = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre + ' ' + self.apellido + ', ' + self.edad + ', ' + self.peso

class InformacionSalud(models.Model):
    frequenciaCardiaca = models.CharField(verbose_name="Frequencia Cardiaca(Heart Rate)", max_length=65)
    saturacionOxigeno = models.CharField(verbose_name="Saturacion De Oxigeno en Sangre", max_length=65)
    nivelEstres = models.CharField(verbose_name="Nivel De Estres", max_length=1, choices=NivelEstres.choices)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)

    def __str__(self):
        return  self.persona.nombre + ' ' + self.persona.apellido + '=> Frequencia Cardiaca:' + self.frequenciaCardiaca + ', ' + self.saturacionOxigeno + ', ' + self.nivelEstres + ', ' + str(self.fecha_creacion)
