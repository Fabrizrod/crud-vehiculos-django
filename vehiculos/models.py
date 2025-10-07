from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    pais = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    modelo = models.CharField(max_length=120)
    ano = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.placa} - {self.modelo}"
