from django.db import models

class Venta(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    id_reloj = models.IntegerField()
    id_cliente = models.IntegerField()
    precio_de_venta = models.IntegerField()
    forma_de_pago = models.CharField(max_length=255)
    estado_de_entrega = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.id
