# Generated by Django 5.0.2 on 2024-03-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0029_image_description_alter_image_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="description",
        ),
        migrations.RemoveField(
            model_name="image",
            name="main_model",
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.FileField(upload_to="fotos/"),
        ),
    ]