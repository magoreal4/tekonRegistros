# Generated by Django 5.0.2 on 2024-02-26 20:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "formularios",
            "0008_formulario1_accesositio_formulario1_adicionales_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="formulario1",
            name="accesoSitio",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="adicionales",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="capacidadEnergia",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="deslindes",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="dimensiones",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="distEmpalmeSitio",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="latEnergia",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="lonEnergia",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="longitudAcceso",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="longitudAccesoConstuccion",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="obstaculos",
        ),
        migrations.RemoveField(
            model_name="formulario1",
            name="tipoSuelo",
        ),
    ]