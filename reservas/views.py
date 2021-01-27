from django.shortcuts import render
from django.views.generic import View
from .models import Reserva, Mesa, TipoReserva
from clientes.models import Cliente

class CreateTicket(View):
    def get(self, request):
        """info = ["Marcela,Santos,VIP,mmarcesantosb@gmail.com,,", "Eugenia,Manzo,VIP,eugeniamanzo4@gmail.com,,", "Camila,Gandica,VIP,camilaganbo22@gmail.com,,", "Mariana,Arraez,VIP,marianaarraez99@gmail.com,267666379,04245389402", "Nicole,Singer,VIP,nicole.singer1809@gmail.com,,", "Leslie,Hallado,VIP,halladoleslie@gmail.com,,", "Sabrina,Valladares,GENERAL,sabrinavalladarest05@gmail.com,,", "Fernanda,Umanes,GENERAL,ferumanes@gmail.com,,", "Isabella,Romandini,GENERAL,sabella1804@gmail.com,,", "María Valeria,Carta,GENERAL,mariavaleriacarta@gmail.com,,", "Korina,Landa,GENERAL,landakorina@gmail.com,,", "Andrea,Osio,GENERAL,aosio2311@hotmail.com,,04144338661", "Gabriela,Osio,GENERAL,osiogabriela10@gmail.com,,04244428595", "Laura,Lleras,GENERAL,laura16lleras@gmail.com,,04244529835", "Isabel,Lleras,GENERAL,isa.Lleras@hotmail.com,,04127667048", "Oriana,Franco,GENERAL,orianafrancos66@gmail.com,,"]             
        for row in info:
            campos = row.split(',')
            #reserva = Reserva()            
            reserva = Reserva.objects.get(cliente__correo=campos[3])
            #reserva.cliente = Cliente.objects.get(correo=campos[3])

            if campos[2]=="VIP":
                reserva.mesa = Mesa.objects.get(pk=2)
            else:
                reserva.mesa = Mesa.objects.get(pk=1)
                                                                            
            #reserva.tipo_reserva = TipoReserva.objects.get(pk=2)
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