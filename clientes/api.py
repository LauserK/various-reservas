# -*- coding: utf-8 -*-
from django.views.generic import View
from django.http import JsonResponse
from django.db import connection, connections
from django.forms.models import model_to_dict
import json, math, datetime
from django.db.models import F

from .models import Cliente

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

class Clientes(View):
    def get(self, request):
        return APIResponse(None, "Bad request", True)

    def post(self, request):                  
        nombre = request.POST.get('nombre')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        estado = request.POST.get('estado')
        ciudad = request.POST.get('ciudad')
        instagram = request.POST.get('instagram')
        host = request.POST.get('host')

        if (nombre != "" and cedula != "" and email != ""):
            cliente = Cliente()

            clientes = Cliente.objects.filter(ci=cedula)
            if len(clientes) <= 0:                                        
                clientes = Cliente.objects.filter(correo=email)

            if len(clientes) > 0:
                cliente = clientes[0]

            cliente.nombre = nombre
            cliente.ci = cedula 
            cliente.telefono = telefono
            cliente.correo = email
            cliente.estado = estado
            cliente.ciudad = ciudad
            cliente.instagram = instagram
            cliente.host = host      
            cliente.save()          


        return APIResponse(None, "Cliente creado", True)