from django.db import models

class Cliente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    correo_electronico = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre