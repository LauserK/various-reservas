# Generated by Django 3.1.5 on 2021-01-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20210115_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='codigo',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
