from django.db import models

class Reloj(models.Model):
    id=models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    precio = models.IntegerField()
    anio_de_lanzamiento = models.IntegerField()

    def __str__(self) -> str:
        return self.marca
