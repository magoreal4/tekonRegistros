# Generated by Django 5.0.2 on 2024-02-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0002_formulario1_accesositio_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulario1",
            name="proveedorEnergia",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
