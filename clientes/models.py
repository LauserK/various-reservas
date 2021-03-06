from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    ci = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=15,blank=True)
    correo = models.EmailField(max_length=254, blank=True)
    estado = models.CharField(max_length=20, blank=True)
    ciudad = models.CharField(max_length=20, blank=True)
    host = models.CharField(max_length=20, blank=True)
    instagram = models.CharField(max_length=20, blank=True)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ci} - {self.nombre}'