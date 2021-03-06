# Generated by Django 3.1.5 on 2021-01-25 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0010_auto_20210121_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesa',
            name='cant_covers',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Covers'),
        ),
        migrations.AlterField(
            model_name='mesa',
            name='numero',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('sinreclamar', 'Sin Reclamar'), ('escaneado', 'Escaneado'), ('reclamado', 'Reclamado')], default='sinreclamar', max_length=50),
        ),
    ]
