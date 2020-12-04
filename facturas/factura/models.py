from enum import unique
from django.db import models

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    num = models.IntegerField()
    anio = models.DateTimeField(auto_now=True)
    cliente_nombre = models.CharField(max_length=220)
    cliente_direccion = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.num}: {self.cliente_nombre}"

class LineaFactura(models.Model):
    id_linea = models.AutoField(primary_key=True)
    factura = models.ForeignKey(
        Factura, 
        on_delete=models.CASCADE)                       # Borramos la línea de la factura, 
    nombre_producto = models.CharField(max_length=220)  # porque la factura no existirá, 
    precio_unitario = models.FloatField()               # y no tendría sentido asignar esa línea a otra factura
    unidades = models.IntegerField()

    def __str__(self):
        return f"{self.unidades}: {self.nombre_producto} - {self.precio_unitario}€"