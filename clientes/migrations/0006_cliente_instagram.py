# Generated by Django 3.1.5 on 2021-03-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210306_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='instagram',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]