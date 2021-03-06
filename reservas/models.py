from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from clientes.models import Cliente
import datetime

# Create your models here.
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Evento(models.Model):
    fecha = models.DateField(default=datetime.date.today, auto_now_add=False)
    nombre = models.CharField(max_length=50)
    locacion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.fecha} - {self.nombre}"

class Zona(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cover(models.Model):
    zona = models.ForeignKey("reservas.Zona", on_delete=models.CASCADE)
    cant_inicial = models.IntegerField(validators = [MinValueValidator(1)])    

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    numero = models.IntegerField(validators = [MinValueValidator(0)])
    zona = models.ForeignKey("reservas.Zona", on_delete=models.CASCADE)
    reservada = models.BooleanField(default=False)
    en_uso = models.BooleanField(default=False)
    cant_covers = models.IntegerField(verbose_name="Cantidad de Covers", default=1, validators = [MinValueValidator(0)])
    articulos = models.ManyToManyField("reservas.ReservaLinea", verbose_name="Articulos de la mesa", blank=True)

    def __str__(self):

        if self.numero == 0:
            return f'{self.zona}'
        return f'{self.zona} - {self.numero}'


class TipoReserva(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class ReservaLinea(models.Model):
    articulo = models.ForeignKey("reservas.Articulo", on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators = [MinValueValidator(1)])

    def __str__(self):
        return f'{self.articulo} x {self.cantidad}'

class Reserva(models.Model):
    evento = models.ForeignKey("reservas.Evento", verbose_name=("Evento"), on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)    
    codigo = models.CharField(blank=True,max_length=10, unique=True)
    cliente = models.ForeignKey("clientes.Cliente", on_delete=models.CASCADE)
    mesa = models.ForeignKey("reservas.Mesa", on_delete=models.CASCADE)    
    precio = models.FloatField(null=True,blank=True, validators = [MinValueValidator(1)])
    #zona = models.ForeignKey("reservas.Zona", on_delete=models.CASCADE)
    articulos = models.ManyToManyField("reservas.ReservaLinea", verbose_name="Articulos de la mesa", blank=True)
    cant_covers_adicional = models.IntegerField(verbose_name="Cantidad de Covers Adicionales", default=0, validators = [MinValueValidator(0)])
    tipo_reserva = models.ForeignKey("reservas.TipoReserva", verbose_name=("Tipo de reserva"), on_delete=models.CASCADE, null=True)
    estados  = (
        ('sinreclamar', 'Sin Reclamar'),
        ('escaneado', 'Escaneado'),
        ('reclamado', 'Reclamado'),
	)
    estado   = models.CharField(max_length=50, choices=estados, default="sinreclamar")

    def __str__(self):
        return f'Reserva de {self.cliente.nombre}, Mesa: #{self.mesa.numero}, Zona: {self.mesa.zona.nombre}'

    def get_total(self):
        return self.cant_covers_adicional + self.mesa.cant_covers

    def save(self, *args, **kwargs):      
        if self.codigo == "" or self.codigo == None:
            code = id_generator(10)  
            exist = Reserva.objects.filter(codigo=code)
        
            if len(exist) > 0:
                code = id_generator(10)  

            self.codigo = code
        super().save(*args, **kwargs)