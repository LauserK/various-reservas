from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    ci = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return f'{self.ci} - {self.nombre}'