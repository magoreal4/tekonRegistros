# Generated by Django 5.0.2 on 2024-03-04 00:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0033_delete_attachment"),
        ("imagenes", "0010_image_etapa_image_sitio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="etapa",
            field=models.CharField(
                choices=[("txtss", "TX/TSS"), ("preIngenieria", "Pre Ingeniería")],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="sitio",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="formularios.sitio",
                verbose_name="Sitio Cod PTI",
            ),
        ),
    ]