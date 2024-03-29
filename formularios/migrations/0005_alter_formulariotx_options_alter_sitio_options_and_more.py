# Generated by Django 5.0.2 on 2024-02-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0004_rename_formulario1_formulariotx"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="formulariotx",
            options={
                "verbose_name": "Formulario TX",
                "verbose_name_plural": "Formularios TX",
            },
        ),
        migrations.AlterModelOptions(
            name="sitio",
            options={"verbose_name": "Sitio", "verbose_name_plural": "Sitios"},
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="lat_inmobiliaria",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="lat_nominal",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="lon_inmobiliaria",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="formulariotx",
            name="lon_nominal",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="sitio",
            name="lat_inmobiliaria",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="sitio",
            name="lat_mandato",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="sitio",
            name="lat_nominal",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="sitio",
            name="lon_inmobiliaria",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="sitio",
            name="lon_mandato",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="sitio",
            name="lon_nominal",
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
    ]
