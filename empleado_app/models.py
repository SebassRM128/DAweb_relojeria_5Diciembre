from django.db import models

class Empleado(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=255)
    anios_experiencia = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
