from django.db import models
from .validators import validar_longitud_sitio, validar_latitud, validar_longitud
from geopy.distance import geodesic
from django.contrib.auth.models import User

class Sitio(models.Model):
    PTICellID = models.CharField(max_length=100)
    EntelID = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=100, blank=True)
    Comuna = models.CharField(max_length=20, blank=True)
    Provincia = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.PTICellID


class Formulario1(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formularios')
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)
    entel_id = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    comuna = models.CharField(max_length=20, blank=True)
    provincia = models.CharField(max_length=50, blank=True)
    lat = models.FloatField(validators=[validar_latitud])
    lon = models.FloatField(validators=[validar_longitud])
    dimensiones = models.CharField(max_length=100)
    deslindes = models.CharField(max_length=100)
    accesoSitio = models.TextField()
    accesoSitioConstruccion = models.TextField()
    longitudAcceso = models.IntegerField(validators=[validar_longitud_sitio])
    longitudAccesoConstuccion = models.IntegerField(validators=[validar_longitud])
    tipoSuelo = models.TextField()
    obstaculos = models.TextField(default="Sin obstaculos")
    adicionales = models.TextField(default="Sin adicionales")
    proveedorEnergia = models.CharField(max_length=100, blank=True)
    latEnergia = models.FloatField(validators=[validar_latitud], blank=True, null=True)
    lonEnergia = models.FloatField(validators=[validar_longitud], blank=True, null=True )
    capacidadEnergia = models.CharField(max_length=20, blank=True)
    distanciaEmpalmeSitio = models.IntegerField(blank=True, null=True)
        
    def calcular_distancia_geopy(self):
        """Calcula la distancia entre el sitio y el punto de energía usando geopy."""
        if self.latEnergia is not None and self.lonEnergia is not None:
            sitio_coords = (self.lat, self.lon)
            energia_coords = (self.latEnergia, self.lonEnergia)
            
            # Calcula la distancia usando geodesic de geopy
            distancia = geodesic(sitio_coords, energia_coords).meters
            return distancia
        else:
            return 0

    def save(self, *args, **kwargs):
        if self.sitio:  # Asegura que el sitio esté establecido
            self.entel_id = self.sitio.EntelID
            self.nombre = self.sitio.Nombre
            self.comuna = self.sitio.Comuna
            self.provincia = self.sitio.Provincia  
            # Calcular la distancia usando geopy antes de guardar
            self.distanciaEmpalmeSitio = self.calcular_distancia_geopy()
        super(Formulario1, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.sitio)
