# Generated by Django 5.0.2 on 2024-03-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0036_remove_sitio_lat_base_remove_sitio_lon_base_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitio",
            name="lat_base",
            field=models.FloatField(
                blank=True,
                max_length=10,
                null=True,
                verbose_name="Latitud Inmobiliaria/Mandato",
            ),
        ),
        migrations.AddField(
            model_name="sitio",
            name="lon_base",
            field=models.FloatField(
                blank=True,
                max_length=10,
                null=True,
                verbose_name="Longitud Inmobiliaria/Mandato",
            ),
        ),
    ]
