# Generated by Django 5.0.2 on 2024-03-02 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "formularios",
            "0019_alter_formulariopreing_longitudaccesoconstuccion_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="sitio",
            name="altura",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="formulariopreing",
            name="sitio",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="formularios.sitio",
                verbose_name="Sitio Cod PTI",
            ),
        ),
        migrations.AlterField(
            model_name="formulariotx",
            name="sitio",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="formularios.sitio",
                verbose_name="Sitio Cod PTI",
            ),
        ),
    ]
