# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection, connections
from django.forms.models import model_to_dict
import json, math, datetime
from django.db.models import F

#import models
from .models import Reserva, Cliente, Mesa, Articulo, Cover

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def APIResponse(data, message, success):
	settings = {
		"success": success,
		"message": message
	}
	if data is not None:
		return JsonResponse({"data": data, "settings":settings})
	else:
		return JsonResponse({"data": [], "settings": settings})

class Reservas(View):
    def get(self, request, ticket_code):
        reservas = list(Reserva.objects.filter(codigo=ticket_code).values())                

        for reserva in reservas:
            reserva_object = Reserva.objects.select_related('cliente').select_related('tipo_reserva').select_related('mesa').get(pk=reserva["id"])
            cliente = reserva_object.cliente
            articulos = reserva_object.articulos.annotate(articulo_nombre=F('articulo__nombre')).all().values()
            mesa = reserva_object.mesa
            tipo_reserva = reserva_object.tipo_reserva
            reserva["cliente_nombre"] =  cliente.nombre
            reserva["cant_covers_mesa"] =  mesa.cant_covers
            reserva["zona"] =  mesa.zona.nombre
            reserva["mesa"] =  f"{mesa.zona} - {mesa.numero}"
            reserva["tipo_reserva"] = tipo_reserva.nombre
            reserva["articulos"] = list(articulos)            

        data = reservas
        
        return APIResponse(data, "Reservas", True)
    
    def post(self, request, ticket_code):
        reserva = Reserva.objects.filter(codigo=ticket_code)

        if len(reserva) > 0:
            reserva[0].estado = "reclamado"
            reserva[0].save()
            return APIResponse(None, "Reserva actualizada", True)
        else:                
            return APIResponse(None, "Reserva no existe", False)