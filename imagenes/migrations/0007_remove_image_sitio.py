# Generated by Django 5.0.2 on 2024-03-03 23:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("imagenes", "0006_image_sitio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="sitio",
        ),
    ]
