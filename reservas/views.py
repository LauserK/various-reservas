from django.shortcuts import render
from django.views.generic import View
from .models import Reserva, Mesa, TipoReserva,Zona
from clientes.models import Cliente
from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import qrcode
import tempfile
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from pathlib import Path
import os

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
            reserva = reservas[0]

        #subject = 'Subject'
        html_message = render_to_string('reservas/ticket_prueba.html', {'reserva': reserva})
        #plain_message = strip_tags(html_message)
        #from_email = 'From <sensevenezuela.val@gmail.com'
        #to = 'kildarealauser@gmail.com'
        #mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
        qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(reserva.codigo)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        
        img.save(os.path.join(BASE_DIR, 'media/'+reserva.codigo+".jpg"),'JPEG')        

        msg = MIMEMultipart()
        msg['Subject'] = '🔵 BLUE EDITION 🔵'
        msg['From'] = 'S E N S E'
        msg['To'] = reserva.cliente.correo
        #msg['To'] = "sensevenezuela.val@gmail.com"
        tmp = open(os.path.join(BASE_DIR, 'media/'+reserva.codigo+".jpg"),'rb')
        image = MIMEImage(tmp.read())
        msg.add_header('Content-Disposition','attachment; filename="%s"' % "codigo-qr.jpg")
        msg.attach(image)
        
        #part1 = MIMEText(html_message, 'plain')
        part2 = MIMEText(html_message, 'html')
        msg.attach(part2)
        #msg.attach(part1)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("sensevenezuela.val@gmail.com", "sense.vzla")
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
        

        ctx = {"reserva": reserva}
        template   = "reservas/ticket.html"
        template   = "reservas/ticket_prueba.html"
        return render(request, template, ctx)