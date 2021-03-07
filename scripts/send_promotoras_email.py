import csv
import os
from pathlib import Path
from clientes.models import Cliente
from reservas.models import Zona, Cover, Mesa, Reserva, ReservaLinea, Articulo, TipoReserva, Evento

def run():	
		
	line_count = 0
	BASE_DIR = Path(__file__).resolve().parent

	archivo = open(os.path.join(BASE_DIR, 'girl.txt'),"r")
	
	for registro in archivo:
		# creamos array de datos de la linea
		campos = registro.split(',')
		
		nombre = campos[2]
		cedula = campos[3]
		telefono = campos[4]
		instagram = campos[5]
		correo = campos[6]

		clientes =[]
		if correo != "":
			clientes = Cliente.objects.filter(correo=correo)
		elif cedula != "":
			clientes = Cliente.objects.filter(ci=cedula)
		else:
			clientes = Cliente.objects.filter(nombre=nombre)

		cliente = None

		if len(clientes) > 0:
			cliente = clientes[0]

			cliente.nombre = nombre
			cliente.ci = cedula
			cliente.instagram = instagram
			cliente.correo = correo
			cliente.telefono = telefono
			cliente.save()
		else:
			cliente = Cliente()
			cliente.nombre = nombre
			cliente.ci = cedula
			cliente.instagram = instagram
			cliente.correo = correo
			cliente.telefono = telefono
			cliente.save()


		evento = Evento.objects.get(pk=2)
		# crear reserva
		reservas = Reserva.objects.filter(cliente = cliente).filter(evento=evento)

		print(reservas)

		if len(reservas)==0:
			zona = Zona.objects.get(pk=9)			
			mesa = Mesa.objects.get(pk=4)

			reserva = Reserva()
			reserva.zona = zona
			reserva.evento = evento
			reserva.cliente = cliente
			reserva.mesa = mesa
			reserva.cant_covers_adicional = 1
			reserva.estado = "sinreclamar"
			reserva.save()		

		else:
			print(line_count)




			#habitacion lentes toallas


