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
    lat_nominal = models.FloatField(max_length=10, blank=True, null=True)
    lon_nominal = models.FloatField(max_length=10, blank=True, null=True)
    lat_inmobiliaria = models.FloatField(max_length=10, blank=True, null=True)
    lon_inmobiliaria = models.FloatField(max_length=10, blank=True, null=True)
    lat_mandato = models.FloatField(max_length=10, blank=True, null=True)
    lon_mandato = models.FloatField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.PTICellID

    class Meta:
        verbose_name = "Sitio"
        verbose_name_plural = "Sitios"

class FormularioTX(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formularios_tx', null=True, blank=False)
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)
    entel_id = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    comuna = models.CharField(max_length=20, blank=True)
    provincia = models.CharField(max_length=50, blank=True)
    lat = models.FloatField(validators=[validar_latitud])
    lon = models.FloatField(validators=[validar_longitud])
    dimensiones = models.CharField(max_length=100, null=True, blank=False)
    deslindes = models.CharField(max_length=100, null=True, blank=False)
    accesoSitio = models.TextField(null=True, blank=False)
    accesoSitioConstruccion = models.TextField(null=True, blank=False)
    longitudAcceso = models.IntegerField(validators=[validar_longitud_sitio], null=True, blank=False)
    longitudAccesoConstuccion = models.IntegerField(validators=[validar_longitud], null=True, blank=False)
    tipoSuelo = models.TextField(null=True, blank=False)
    obstaculos = models.TextField(default="Sin obstaculos")
    adicionales = models.TextField(default="Sin adicionales")
    proveedorEnergia = models.CharField(max_length=100, blank=True, null=True)
    capacidadEnergia = models.CharField(max_length=20, blank=True)
    
    lat_energia = models.FloatField(validators=[validar_latitud], blank=True, null=True)
    lon_energia = models.FloatField(validators=[validar_longitud], blank=True, null=True )
    distanciaEmpalmeSitio = models.IntegerField(blank=True, null=True)
    
    lat_nominal = models.FloatField(max_length=10, blank=True, null=True)
    lon_nominal = models.FloatField(max_length=10, blank=True, null=True)
    
    lat_inmobiliaria = models.FloatField(max_length=10, blank=True, null=True)
    lon_inmobiliaria = models.FloatField(max_length=10, blank=True, null=True)
    
    dist_nominal_inmobiliaria = models.IntegerField(blank=True, null=True)
    dist_nominal_inspeccion = models.IntegerField(blank=True, null=True)
    dist_inmobiliaria_inspeccion = models.IntegerField(blank=True, null=True)
    
    comentario = models.TextField(default="Sin comentarios", null=True, blank=True)
    
    def __str__(self):
        return self.entel_id

    def calcular_distancia_geopy(self, lat_1, lon_1, lat_2, lon_2):
        """Calcula la distancia entre dos puntos usando geopy."""
        if lat_1 is not None and lon_1 is not None and lat_2 is not None and lon_2 is not None:
            origen_coords = (lat_1, lon_1)
            destino_coords = (lat_2, lon_2)
            # Calcula la distancia usando geodesic de geopy
            distancia = geodesic(origen_coords, destino_coords).meters
            return distancia
        else:
            return None

    def save(self, *args, **kwargs):
        if self.sitio:  # Asegura que el sitio esté establecido
            self.entel_id = self.sitio.EntelID
            self.nombre = self.sitio.Nombre
            self.comuna = self.sitio.Comuna
            self.provincia = self.sitio.Provincia
            self.lat_nominal = self.sitio.lat_nominal
            self.lon_nominal = self.sitio.lon_nominal
            self.lat_inmobiliaria = self.sitio.lat_inmobiliaria
            self.lon_inmobiliaria = self.sitio.lon_inmobiliaria
            
            # Calcular las distancias usando geopy antes de guardar
            self.distanciaEmpalmeSitio = self.calcular_distancia_geopy(self.lat, self.lon, self.lat_energia, self.lon_energia)
            self.dist_nominal_inmobiliaria = self.calcular_distancia_geopy(self.lat_nominal, self.lon_nominal, self.lat_inmobiliaria, self.lon_inmobiliaria)
            self.dist_nominal_inspeccion = self.calcular_distancia_geopy(self.lat_nominal, self.lon_nominal, self.lat, self.lon)
            self.dist_inmobiliaria_inspeccion = self.calcular_distancia_geopy(self.lat_inmobiliaria, self.lon_inmobiliaria, self.lat, self.lon)
        super(FormularioTX, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.sitio)
    
    class Meta:
        verbose_name = "Formulario TX"
        verbose_name_plural = "Formularios TX"

class FormularioPreIng(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formularios_preing', null=True, blank=False)
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE)
    entel_id = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    comuna = models.CharField(max_length=20, blank=True)
    provincia = models.CharField(max_length=50, blank=True)
    lat = models.FloatField(validators=[validar_latitud])
    lon = models.FloatField(validators=[validar_longitud])
    dimensiones = models.CharField(max_length=100, null=True, blank=False)
    deslindes = models.CharField(max_length=100, null=True, blank=False)
    accesoSitio = models.TextField(null=True, blank=False)
    accesoSitioConstruccion = models.TextField(null=True, blank=False)
    longitudAcceso = models.IntegerField(validators=[validar_longitud_sitio], null=True, blank=False)
    longitudAccesoConstuccion = models.IntegerField(validators=[validar_longitud], null=True, blank=False)
    tipoSuelo = models.TextField(null=True, blank=False)
    obstaculos = models.TextField(default="Sin obstaculos")
    adicionales = models.TextField(default="Sin adicionales")
    proveedorEnergia = models.CharField(max_length=100, blank=True, null=True)
    capacidadEnergia = models.CharField(max_length=20, blank=True)
    
    lat_energia = models.FloatField(validators=[validar_latitud], blank=True, null=True)
    lon_energia = models.FloatField(validators=[validar_longitud], blank=True, null=True )
    distanciaEmpalmeSitio = models.IntegerField(blank=True, null=True)
    
    lat_mandato = models.FloatField(max_length=10, blank=True, null=True)
    lon_mandato = models.FloatField(max_length=10, blank=True, null=True)
    
    dist_mandato_ingenieria = models.IntegerField(blank=True, null=True)
    
    comentario = models.TextField(default="Sin comentarios", null=True, blank=True)

    def calcular_distancia_geopy(self, lat_1, lon_1, lat_2, lon_2):
        """Calcula la distancia entre dos puntos usando geopy."""
        if lat_1 is not None and lon_1 is not None and lat_2 is not None and lon_2 is not None:
            origen_coords = (lat_1, lon_1)
            destino_coords = (lat_2, lon_2)
            # Calcula la distancia usando geodesic de geopy
            distancia = geodesic(origen_coords, destino_coords).meters
            return distancia
        else:
            return None

    def save(self, *args, **kwargs):
        if self.sitio:  # Asegura que el sitio esté establecido
            self.entel_id = self.sitio.EntelID
            self.nombre = self.sitio.Nombre
            self.comuna = self.sitio.Comuna
            self.provincia = self.sitio.Provincia
            self.lat_mandato = self.sitio.lat_mandato
            self.lon_mandato = self.sitio.lon_mandato
            
            # Calcular las distancias usando geopy antes de guardar
            self.distanciaEmpalmeSitio = self.calcular_distancia_geopy(self.lat, self.lon, self.lat_energia, self.lon_energia)
            self.dist_mandato_ingenieria = self.calcular_distancia_geopy(self.lat_mandato, self.lon_mandato, self.lat, self.lon)
        super(FormularioPreIng, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.sitio)
    
    class Meta:
        verbose_name = "Formulario Pre-Ingenieria"
        verbose_name_plural = "Formularios Pre-Ingenieria"