from django.contrib import admin
from .models import Zona, Cover, Mesa, Reserva, ReservaLinea, Articulo

# Register your models here.

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    pass

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    pass

@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    pass

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    pass

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ['codigo']
    filter_horizontal = ('articulos',)

@admin.register(ReservaLinea)
class ReservaLineaAdmin(admin.ModelAdmin):
    pass