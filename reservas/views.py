from django.shortcuts import render
from django.views.generic import View
from .models import Reserva

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