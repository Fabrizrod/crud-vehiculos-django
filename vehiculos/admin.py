from django.contrib import admin
from .models import Propietario, Vehiculo

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ('dni', 'apellido', 'nombre', 'pais', 'telefono')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'ano', 'propietario')
