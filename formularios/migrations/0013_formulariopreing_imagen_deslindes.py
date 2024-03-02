# Generated by Django 5.0.2 on 2024-03-01 22:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0012_alter_formulariopreing_dist_mandato_ingenieria_and_more"),
        ("main", "0002_alter_image_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="formulariopreing",
            name="imagen_deslindes",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="main.image",
            ),
        ),
    ]
