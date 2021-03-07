from django.contrib import admin
from django.shortcuts import redirect
from .models import Zona, Cover, Mesa, Reserva, ReservaLinea, Articulo, TipoReserva, Evento

# Register your models here.

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

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
    list_display = ('cliente','codigo','mesa','tipo_reserva','estado')
    list_filter = ('mesa__zona','evento')
    filter_horizontal = ('articulos',)    

    def response_add(self, request, obj, post_url_continue=None):        
        return redirect('/reservas/ticket/'+obj.codigo)

@admin.register(ReservaLinea)
class ReservaLineaAdmin(admin.ModelAdmin):
    pass