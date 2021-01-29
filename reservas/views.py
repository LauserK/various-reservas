from django.shortcuts import render
from django.views.generic import View
from .models import Reserva, Mesa, TipoReserva,Zona
from clientes.models import Cliente

class TicketReportHome(View):
    def get(self, request):
        reservas = Reserva.objects.all().order_by('mesa__zona__nombre').order_by('cliente__nombre')
        zonas =  Zona.objects.all()
        template   = "reservas/reporte.html"
        return render(request, template, {"reservas":reservas, "zonas":zonas})


class CreateTicket(View):
    def get(self, request):
        info = ["Jose Antonio,Lopez,VIP,joselopezpayares25@gmail.com,,","Jonas,Alvarez,VIP,jonasa87@gmail.com,V17449755,04144042752","Julio,Miranda,VIP,juliojmirandas@gmail.com,V20181069,","Alejandro,Hermanavicius,VIP,hermanaviciusa@gmail.com,V20181706,04144361632"]
        for row in info:
            campos = row.split(',')
            reserva = Reserva()         
            cliente = Cliente()
            """
            try:
                cliente = Cliente.objects.get(correo=campos[3])
            except:
                cliente = Cliente()
                cliente.nombre = f"{campos[0]} {campos[1]}"   
                cliente.ci = campos[4]
                cliente.correo = campos[3]
                cliente.telefono = campos[5]
                cliente.save()
            
            reserva = Reserva()
            reserva.cliente = cliente

            if campos[2]=="VIP":
                reserva.mesa = Mesa.objects.get(pk=2)
            #else:
            #    reserva.mesa = Mesa.objects.get(pk=1)
                                                                            
            reserva.tipo_reserva = TipoReserva.objects.get(pk=2)
            reserva.save()            
            """
        template   = "reservas/ticket.html"
        return render(request, template, {})

# Create your views here.
class TicketView(View):
    def get(self, request, ticket_code):
        reservas = Reserva.objects.filter(codigo=ticket_code)
        reserva = None
        if len(reservas) > 0:
            reserva = Reserva.objects.get(codigo=ticket_code)
        ctx = {"reserva": reserva}
        template   = "reservas/ticket.html"
        return render(request, template, ctx)