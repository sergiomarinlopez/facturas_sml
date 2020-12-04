from factura.apps import FacturaConfig
from django.shortcuts import render
from factura.models import Factura, LineaFactura

# Create your views here.

def homepage(request):
    return render(request, 'factura/homepage.html', {
        "facturas": Factura.objects.all().order_by('-anio'),
        })

def detalle_factura(request, id_factura):
    return render(request, 'factura/detalle_factura.html', {
        'lineas': LineaFactura.objects.filter(factura=id_factura),
        })
