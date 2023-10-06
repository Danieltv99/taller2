from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    pacientes = models.ManyToManyField('Paciente', related_name='doctores')

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    doctor_asignado = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='pacientes_asignados')

class Meta:
     db_table = 'doctores' #nombre de instancia con la que llamamos la tabla en la Base de Datos
     db_table2 = 'pacientes'
