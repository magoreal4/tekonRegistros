# Generated by Django 5.0.2 on 2024-03-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("imagenes", "0016_image_sitio"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormularioTX",
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
                (
                    "etapa",
                    models.CharField(
                        choices=[
                            ("txtss", "TX/TSS"),
                            ("preIngenieria", "Pre Ingeniería"),
                        ],
                        default="txtss",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="image",
            name="etapa",
            field=models.CharField(
                choices=[("txtss", "TX/TSS"), ("preIngenieria", "Pre Ingeniería")],
                default=1,
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
