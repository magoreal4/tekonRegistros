# Generated by Django 5.0.2 on 2024-03-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("imagenes", "0014_delete_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pic", models.FileField(upload_to="fotografias/")),
            ],
        ),
    ]