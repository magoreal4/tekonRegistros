# Generated by Django 5.0.2 on 2024-03-01 22:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0015_alter_formulariopreing_imagen_deslindes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="formulariopreing",
            name="imagen_deslindes",
        ),
    ]
