# Generated by Django 3.1.5 on 2021-03-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_cliente_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='instagram',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]