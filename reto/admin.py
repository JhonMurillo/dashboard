from django.contrib import admin
from django.utils.html import mark_safe
from .models import Persona, InformacionSalud
from django.contrib.auth.models import User, Group
from django.contrib.admin.options import TabularInline
from django.db.models import Q, Count

# Register your models here.
# admin.site.register(InformacionSalud)

admin.site.unregister(User)
admin.site.unregister(Group)

class InformacionSaludAInline(TabularInline):
    extra = 1
    model = InformacionSalud
    fields  = ('frequenciaCardiaca', 'saturacionOxigeno', 'nivelEstres',)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'apellido', 'edad', 'peso', 'count_informacion')
    list_display_links = ('pk', 'nombre', 'apellido')
    search_fields = ['nombre', 'apellido']
    inlines = [InformacionSaludAInline]

    def count_informacion(self, obj):
        count_information = InformacionSalud.objects.filter(persona=obj)
        return count_information.count()