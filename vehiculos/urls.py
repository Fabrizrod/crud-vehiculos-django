from django.urls import path
from . import views

urlpatterns = [
    # Vehículos
    path('', views.lista_vehiculos, name='lista_vehiculos'),
    path('crear/', views.crear_vehiculo, name='crear_vehiculo'),
    path('editar/<int:id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar/<int:id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),

    # Propietarios
    path('propietarios/', views.lista_propietarios, name='lista_propietarios'),
    path('propietarios/crear/', views.crear_propietario, name='crear_propietario'),
    path('propietarios/editar/<int:id>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),
]
