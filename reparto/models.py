from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, unique=True, max_length=6, null=False, blank=False)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=20, null=False)
    year = models.IntegerField(null=False)
 
class Chofer(models.Model):
    rut = models.CharField(primary_key=True, unique=True, max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

class RegistroContabilidad(models.Model):
    id = models.AutoField(primary_key=True)
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=False)
    valor = models.FloatField(null=False)
    fecha_compra = models.DateField(null=False)
    
    



