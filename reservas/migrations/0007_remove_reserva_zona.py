# Generated by Django 3.1.5 on 2021-01-18 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0006_auto_20210115_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='zona',
        ),
    ]