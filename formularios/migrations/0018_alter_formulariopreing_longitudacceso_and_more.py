# Generated by Django 5.0.2 on 2024-03-02 03:01

import formularios.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0017_remove_formulariotx_dist_nominal_inmobiliaria_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulariopreing",
            name="longitudAcceso",
            field=models.IntegerField(
                null=True,
                validators=[formularios.validators.validar_longitud_sitio],
                verbose_name="Longitud Acceso (m)",
            ),
        ),
        migrations.AlterField(
            model_name="formulariopreing",
            name="longitudAccesoConstuccion",
            field=models.IntegerField(
                null=True,
                validators=[formularios.validators.validar_longitud],
                verbose_name="Longitud Acceso Construccion (m)",
            ),
        ),
        migrations.AlterField(
            model_name="formulariotx",
            name="longitudAcceso",
            field=models.IntegerField(
                null=True,
                validators=[formularios.validators.validar_longitud_sitio],
                verbose_name="Longitud Acceso (m)",
            ),
        ),
        migrations.AlterField(
            model_name="formulariotx",
            name="longitudAccesoConstuccion",
            field=models.IntegerField(
                null=True,
                validators=[formularios.validators.validar_longitud],
                verbose_name="ongitud Acceso Construccion (m)",
            ),
        ),
    ]