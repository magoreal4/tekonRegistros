# Generated by Django 5.0.2 on 2024-02-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0005_alter_formulariotx_options_alter_sitio_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulariotx",
            name="dist_inmobiliaria_inspeccion",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="dist_nominal_inmobiliaria",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="dist_nominal_inspeccion",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
