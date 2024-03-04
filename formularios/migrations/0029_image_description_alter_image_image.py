# Generated by Django 5.0.2 on 2024-03-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("formularios", "0028_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="fotos/"),
        ),
    ]
