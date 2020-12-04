from django.contrib import admin

from factura.models import Factura, LineaFactura

class FacturaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Factura, FacturaAdmin)

class LineaFacturaAdmin(admin.ModelAdmin):
    pass

admin.site.register(LineaFactura, LineaFacturaAdmin)

