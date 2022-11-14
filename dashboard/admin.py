from django.contrib import admin
# from django.utils.html import mark_safe
from .models import Persona, InformacionSalud, CalidadVida
# from django.contrib.auth.models import User, Group
# from django.contrib.admin.options import TabularInline
# from django.db.models import Q, Count

# # Register your models here.
# admin.site.register(CalidadVida)

# admin.site.unregister(User)
# admin.site.unregister(Group)

# class InformacionSaludAInline(TabularInline):
#     extra = 1
#     model = InformacionSalud
#     fields  = ('frequenciaCardiaca', 'saturacionOxigeno', 'nivelEstres',)


# @admin.register(Persona)
# class PersonaAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'nombre', 'apellido', 'edad', 'peso', 'count_informacion')
#     list_display_links = ('pk', 'nombre', 'apellido')
#     search_fields = ['nombre', 'apellido']
#     inlines = [InformacionSaludAInline]

#     def count_informacion(self, obj):
#         count_information = InformacionSalud.objects.filter(persona=obj)
#         return count_information.count()

@admin.register(CalidadVida)
class CalidadVidaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'categoria', 'sub_categoria', 'rango', 'cantidad', 'fecha_creacion')
    list_display_links = ('pk', 'categoria', 'sub_categoria')
    search_fields = ['categoria', 'sub_categoria']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return self.readonly_fields + ('categoria', 'sub_categoria', 'rango')
        return self.readonly_fields

    def has_delete_permission(self, request, obj=None):
        return False