from django.db import models
from .validators import validar_longitud_sitio, validar_latitud, validar_longitud
from geopy.distance import geodesic
from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile
from main.models import Image
from django.utils import timezone
from django.templatetags.static import static

def obtener_imagen_google_maps(latitud, longitud, lat_mandato, lon_mandato, lat_energia, lon_energia, zoom=18, maptype="hybrid", scale=2, tamano="640x400"):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    api_key = "AIzaSyD22EmbDEXIc7Meum5e2MCYj4D0JpDrmpU"


    # Verificar si lat_mandato y lon_mandato son válidos
    if lat_mandato in [None, ""] or lon_mandato in [None, ""]:
        centro = f"{latitud},{longitud}"
        if lat_energia in [None, ""] or lon_energia in [None, ""]:
            markers = [
                f"size:mid|color:0xFFFF00|label:I|{latitud},{longitud}",
                ]
        else:
            markers = [
                f"size:mid|color:0xFFFF00|label:I|{latitud},{longitud}",
                f"size:tiny|color:0x00FFFF|{lat_energia},{lon_energia}",
            ]
    else:
        # Si son válidos, calcular promedio para el centro y usar ambos para marcadores¡
        promedio_latitud = (latitud + lat_mandato) / 2
        promedio_longitud = (longitud + lon_mandato) / 2
        centro = f"{promedio_latitud},{promedio_longitud}"
        markers = [
            f"size:normal|color:0x00FF00|label:M|{lat_mandato},{lon_mandato}",
            f"size:mid|color:0xFFFF00|label:I|{latitud},{longitud}",
            f"size:tiny|color:0x00FFFF|{lat_energia},{lon_energia}",
        ]
    # print(imagen_content)
    params = {
        "center": centro,
        "zoom": zoom,
        "size": tamano,
        "maptype": maptype,  # "roadmap" Agrega este parámetro para obtener imágenes satelitales
        "scale" : scale,
        "key": api_key,
        "markers": markers,  # Agrega un marcador rojo con la etiqueta 'A'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:

        return response.content
    else:
        return None


class Sitio(models.Model):
    PTICellID = models.CharField(max_length=100)
    EntelID = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=100, blank=True)
    Comuna = models.CharField(max_length=20, blank=True)
    Provincia = models.CharField(max_length=50, blank=True)
    altura = models.CharField(max_length=100, blank=True, null=True)
    lat_base = models.FloatField(max_length=10, blank=True, null=True, verbose_name='Latitud Inmobiliaria/Mandato')
    lon_base = models.FloatField(max_length=10, blank=True, null=True, verbose_name='Longitud Inmobiliaria/Mandato')


    def __str__(self):
        return self.PTICellID

    class Meta:
        verbose_name = "Sitio"
        verbose_name_plural = "Sitios"

ETAPA_CHOICES = (
    ('txtss', 'TX/TSS'),
    ('preIngenieria', 'Pre Ingeniería'),
)


class FormularioTX(models.Model):
    etapa = models.CharField(max_length=20, choices=ETAPA_CHOICES, default="txtss")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formularios_1', null=True, blank=False)
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, verbose_name='Sitio Cod PTI')
    entel_id = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    comuna = models.CharField(max_length=20, blank=True)
    provincia = models.CharField(max_length=50, blank=True)
    lat = models.FloatField(validators=[validar_latitud], verbose_name='Latitud Inspeccion')
    lon = models.FloatField(validators=[validar_longitud], verbose_name='Longitud Inspeccion')
    dimensiones = models.CharField(max_length=100, null=True, blank=False)
    deslindes = models.CharField(max_length=100, null=True, blank=False)
    accesoSitio = models.TextField(null=True, blank=False, verbose_name='Acceso al Sitio' )
    accesoSitioConstruccion = models.TextField(null=True, blank=False, verbose_name='Acceso al Sitio para Construccion')
    longitudAcceso = models.IntegerField(validators=[validar_longitud_sitio], null=True, blank=False, verbose_name='Longitud Acceso (m)')
    longitudAccesoConstuccion = models.IntegerField(validators=[validar_longitud_sitio], null=True, blank=False, verbose_name='Longitud Acceso Construccion (m)')
    tipoSuelo = models.TextField(null=True, blank=False, verbose_name='Tipo de Suelo')
    obstaculos = models.TextField(default="Sin obstaculos")
    adicionales = models.TextField(default="Sin adicionales", verbose_name='Trabajos Adicionales')
    proveedorEnergia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Proveedor de Energía')
    capacidadEnergia = models.CharField(max_length=20, blank=True, verbose_name='Capacidad de Energia' )
    
    lat_energia = models.FloatField(validators=[validar_latitud], blank=True, null=True, verbose_name='Latitud de Empalme')
    lon_energia = models.FloatField(validators=[validar_longitud], blank=True, null=True, verbose_name='Longitud de Empalme')
    distanciaEmpalmeSitio = models.IntegerField(blank=True, null=True, verbose_name='Distancia de Empalme a Sitio (m)')
    
    lat_base = models.FloatField(max_length=10, blank=True, null=True, verbose_name='Latitud Inmobiliaria/Mandato')
    lon_base = models.FloatField(max_length=10, blank=True, null=True, verbose_name='Longitud Inmobiliaria/Mandato')
    
    dist_base_inspeccion = models.IntegerField(blank=True, null=True, verbose_name='Desfase (m)')
    
    comentario = models.TextField(default="Sin comentarios", null=True, blank=True)
    
    imagen = models.ImageField(upload_to='imagenes_mapas/', null=True, blank=True)
    
    altura = models.CharField(max_length=100, blank=True, null=True, verbose_name='Altura (m)')
    
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    def imagen_deslindes(self):
        # Obtén la instancia de Image
        imagen_instance = Image.load()
        if imagen_instance:
            return imagen_instance.image.url
        return None
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
            
            if self.sitio.lat_base is not None and self.sitio.lon_base is not None:
                self.lat_base = self.sitio.lat_base
                self.lon_base = self.sitio.lon_base
            
            else:
                self.sitio.lat_base = self.lat_base
                self.sitio.lon_base = self.lon_base
                self.sitio.save()
                
            # Calcular las distancias usando geopy antes de guardar
            self.distanciaEmpalmeSitio = self.calcular_distancia_geopy(self.lat, self.lon, self.lat_energia, self.lon_energia)
            self.dist_base_inspeccion = self.calcular_distancia_geopy(self.lat_base, self.lon_base, self.lat, self.lon) or 0
            
            if not self.imagen:  # Si no hay imagen ya asociada, obten una nueva
                if self.dist_base_inspeccion>150:
                    imagen_content = obtener_imagen_google_maps(self.lat, self.lon, self.lat_base, self.lon_base, self.lat_energia, self.lon_energia, zoom=15)
                else:
                    imagen_content = obtener_imagen_google_maps(self.lat, self.lon, self.lat_base, self.lon_base, self.lat_energia, self.lon_energia)

                if imagen_content:
                    filename = f"mapa_{self.pk or 'nuevo'}.png"
                    self.imagen.save(filename, ContentFile(imagen_content), save=False)

        super(FormularioTX, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.sitio)
    
    class Meta:
        verbose_name = "Formulario TX/Inmobiliaria"
        verbose_name_plural = "Formularios TX/Inmobiliaria"

