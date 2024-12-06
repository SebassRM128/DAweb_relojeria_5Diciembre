from django.db import models

class Reparacion(models.Model):
    idreparacion = models.IntegerField(null=True,blank=True)
    fecha_recepcion = models.DateField()
    id_reloj = models.IntegerField()
    descripcion_problema = models.TextField(max_length=255)
    costo_de_reparacion = models.IntegerField()
    tiempo_de_reparacion = models.CharField(max_length=30)
    estado_reparacion = models.CharField(max_length=255)
    detalles=models.TextField(max_length=500)
    fecha_entrega=models.DateField()
    id_cliente=models.IntegerField()
    id_empleado=models.IntegerField()


    def __str__(self) -> str:
        return self.descripcion_problema
