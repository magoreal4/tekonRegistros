# Generated by Django 5.0.2 on 2024-03-03 19:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0031_alter_image_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Image",
            new_name="Attachment",
        ),
    ]
