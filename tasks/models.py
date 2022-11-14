from django.db import models


# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "No Iniciada"
    ONGOING = 'o', "En Progreso"
    FINISHED = 'f', "Finalizada"


class Task(models.Model):
    name = models.CharField(verbose_name="Nombre De La Tarea", max_length=65, unique=True)
    status = models.CharField(verbose_name="Estado", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
