from enum import unique
from django.db import models

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    num = models.IntegerField()
    anio = models.DateTimeField(auto_now=True)
    cliente_nombre = models.CharField(max_length=220)
    cliente_direccion = models.CharField(max_length=400)

    @property
    def num_lineas(self):
      return LineaFactura.objects.filter(factura=self.id_factura).count()
    
    @property
    def precio_factura(self):
        lineas = LineaFactura.objects.filter(factura=self.id_factura)
        total = 0
        for l in lineas:
            total += l.precio_real
        return round(total, 2)

    @property
    def precio_factura_iva(self):
        lineas = LineaFactura.objects.filter(factura=self.id_factura)
        total = 0
        for l in lineas:
            total += l.precio_real + l.precio_real*0.21
        return round(total, 2)

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
   
    @property
    def precio_real(self):
      return self.precio_unitario * self.unidades

    def __str__(self):
        return f"{self.unidades}: {self.nombre_producto} - {self.precio_unitario}€"