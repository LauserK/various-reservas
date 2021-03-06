# Generated by Django 3.1.5 on 2021-03-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20210125_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='host',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='cliente',
            name='verificado',
            field=models.BooleanField(default=False),
        ),
    ]
