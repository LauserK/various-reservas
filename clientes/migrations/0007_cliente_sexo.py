# Generated by Django 3.1.5 on 2021-03-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_cliente_instagram'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('hombre', 'Hombre'), ('mujer', 'Mujer')], default='mujer', max_length=10),
        ),
    ]
