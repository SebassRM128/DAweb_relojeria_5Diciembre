from django.db import models

class Reparacion(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    id_reloj = models.IntegerField()
    descripcion_problema = models.TextField(max_length=255)
    costo_de_reparacion = models.IntegerField()
    tiempo_de_reparacion = models.CharField(max_length=30)
    estado_reparacion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descripcion_problema
