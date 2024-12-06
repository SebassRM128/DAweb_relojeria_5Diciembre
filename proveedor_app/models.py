from django.db import models

class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=255)
    numero_de_cuenta = models.IntegerField()
    pais_de_origen = models.CharField(max_length=255)


    def __str__(self) -> str:
        return self.nombre
