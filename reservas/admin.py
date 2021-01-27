from django.contrib import admin
from django.shortcuts import redirect
from .models import Zona, Cover, Mesa, Reserva, ReservaLinea, Articulo, TipoReserva

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

@admin.register(TipoReserva)
class TipoReservaAdmin(admin.ModelAdmin):
    pass

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ['codigo']
    filter_horizontal = ('articulos',)    

    def response_add(self, request, obj, post_url_continue=None):        
        return redirect('/reservas/ticket/'+obj.codigo)

@admin.register(ReservaLinea)
class ReservaLineaAdmin(admin.ModelAdmin):
    pass