# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Sitio, FormularioTX


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Sitio, FormularioTX, FormularioPreIng

# @receiver(post_save, sender=Sitio)
# def update_formulariotx_altura(sender, instance, **kwargs):
#     FormularioTX.objects.filter(sitio=instance).update(altura=instance.altura)
    # FormularioPreIng.objects.filter(sitio=instance).update(lat_mandato=instance.lat_mandato)
    # FormularioPreIng.objects.filter(sitio=instance).update(lon_mandato=instance.lon_mandato)
    # FormularioTX.objects.filter(sitio=instance).update(lat_inmobiliaria=instance.lat_inmobiliaria)
    # FormularioTX.objects.filter(sitio=instance).update(lon_inmobiliaria=instance.lon_inmobiliaria)   
    
# @receiver(post_save, sender=Sitio)
# def update_formulariotx_altura(sender, instance, **kwargs):
#     FormularioPreIng.objects.filter(sitio=instance).update(altura=instance.altura)

# @receiver(post_save, sender=FormularioTX)
# def update_sitio_altura(sender, instance, **kwargs):
#     instance.sitio.altura = instance.altura
#     instance.sitio.save()

# @receiver(post_save, sender=FormularioPreIng)
# def update_sitio_altura(sender, instance, **kwargs):
#     instance.sitio.altura = instance.altura
#     instance.sitio.save()



# @receiver(post_save, sender=Sitio)
# def sync_from_Sitio_to_FormularioPreIng(sender, instance, **kwargs):
#     FormularioPreIng.objects.all().update(lat_mandato=instance.lat_mandato)
#     FormularioPreIng.objects.all().update(lon_mandato=instance.lon_mandato)

# @receiver(post_save, sender=FormularioPreIng)
# def sync_from_FormularioPreIng_to_Sitio(sender, instance, **kwargs):
#     Sitio.objects.all().update(lat_mandato=instance.lat_mandato)
#     Sitio.objects.all().update(lon_mandato=instance.lon_mandato)


# @receiver(post_save, sender=Sitio)
# def sync_from_Sitio_to_FormularioTX(sender, instance, **kwargs):
#     FormularioTX.objects.all().update(lat_inmobiliaria=instance.lat_inmobiliaria)
#     FormularioTX.objects.all().update(lon_inmobiliaria=instance.lon_inmobiliaria)

# @receiver(post_save, sender=FormularioTX)
# def sync_from_FormularioTX_to_Sitio(sender, instance, **kwargs):
#     Sitio.objects.all().update(lat_inmobiliaria=instance.lat_inmobiliaria)
#     Sitio.objects.all().update(lon_inmobiliaria=instance.lon_inmobiliaria)