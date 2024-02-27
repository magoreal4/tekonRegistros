# validators.py
from django.core.exceptions import ValidationError

def validar_longitud_sitio(value):
    if not 0 <= value <= 10000:
        raise ValidationError("La longitud de acceso no puede tener ese valor.")

def validar_latitud(value):
    if not -90 <= value <= 90:
        raise ValidationError("La latitud debe estar entre -90 y 90 grados.")

def validar_longitud(value):
    if not -180 <= value <= 180:
        raise ValidationError("La longitud debe estar entre -180 y 180 grados.")
