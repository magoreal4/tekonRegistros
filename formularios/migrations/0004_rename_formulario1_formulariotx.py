# Generated by Django 5.0.2 on 2024-02-29 14:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0003_alter_formulario1_proveedorenergia"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Formulario1",
            new_name="FormularioTX",
        ),
    ]