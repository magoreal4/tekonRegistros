from django.db import models


ETAPA_CHOICES = (
    ('txtss', 'TX/TSS'),
    ('preIngenieria', 'Pre Ingeniería'),
)


class FormularioTX(models.Model):
    etapa = models.CharField(max_length=20, choices=ETAPA_CHOICES, default="txtss")

class Image(models.Model):
    pic = models.FileField(upload_to='fotografias/')
    sitio = models.CharField(max_length=10)
    etapa = models.CharField(max_length=20, choices=ETAPA_CHOICES)
    descripcion = models.TextField(blank=True, null=True)