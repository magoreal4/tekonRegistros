# Generated by Django 5.0.2 on 2024-03-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "formularios",
            "0025_remove_formulariotx_dist_inmobiliaria_inspeccion_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="formulariotx",
            options={
                "verbose_name": "Formulario TX/Inmobiliaria",
                "verbose_name_plural": "Formularios TX/Inmobiliaria",
            },
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="etapa",
            field=models.CharField(
                choices=[("txtss", "TX/TSS"), ("preIngenieria", "Pre Ingeniería")],
                default="txtss",
                max_length=20,
            ),
        ),
    ]
