# Generated by Django 5.0.2 on 2024-03-03 20:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0032_rename_image_attachment"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Attachment",
        ),
    ]
