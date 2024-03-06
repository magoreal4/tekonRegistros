# Generated by Django 5.0.2 on 2024-03-04 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0033_delete_attachment"),
        ("imagenes", "0011_alter_image_etapa_alter_image_sitio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="sitio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="formularios.sitio",
                verbose_name="Sitio Cod PTI",
            ),
        ),
    ]