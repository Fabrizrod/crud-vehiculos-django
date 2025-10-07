from django import forms
from .models import Vehiculo, Propietario

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'apellido', 'dni', 'telefono', 'pais']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'modelo', 'ano', 'foto', 'propietario']
