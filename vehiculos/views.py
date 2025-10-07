from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Propietario
from .forms import VehiculoForm, PropietarioForm

def lista_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'vehiculos/propietarios_list.html', {'propietarios': propietarios})

def crear_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'vehiculos/form_propietario.html', {'form': form})

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.select_related('propietario').all()
    return render(request, 'vehiculos/vehiculos_list.html', {'vehiculos': vehiculos})

def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/form_vehiculo.html', {'form': form})

def editar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'vehiculos/propietario_form.html', {'form': form})

def eliminar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        propietario.delete()
        return redirect('lista_propietarios')
    return render(request, 'vehiculos/propietario_confirm_delete.html', {'propietario': propietario})

def editar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculos/vehiculo_form.html', {'form': form})

def eliminar_vehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, id=id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'vehiculos/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})



