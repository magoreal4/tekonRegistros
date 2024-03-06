from django.contrib import admin
from .models import FormularioTX, Sitio, User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.utils.html import format_html
from imagenes.models import Image


def dec_to_gms(decimal_deg, is_lat=True):
    if decimal_deg is None or decimal_deg == "":
        return "-"
    # Determina si el grado es negativo (Sur o Oeste)
    is_negative = decimal_deg < 0
    # Convierte el grado a positivo para el cálculo
    decimal_deg = abs(decimal_deg)
    
    degrees = int(decimal_deg)
    minutes = int((decimal_deg - degrees) * 60)
    seconds = (decimal_deg - degrees - minutes/60) * 3600.00

    # Decide el sufijo basado en si es latitud y si es positivo/negativo
    if is_lat:
        suffix = "S" if is_negative else "N"
    else:
        suffix = "O" if is_negative else "E"
    
    return f"{degrees}° {minutes}' {seconds:.2f}\" {suffix}"

class SitiosResource(resources.ModelResource):
    sitio = fields.Field(column_name='PTI Cell ID',attribute='PTICellID',)
    entel_id = fields.Field(column_name='ID Entel', attribute='EntelID')
    nombre = fields.Field(column_name='Nombre', attribute='Nombre')
    comuna = fields.Field(column_name='Comuna', attribute='Comuna')
    provincia = fields.Field(column_name='Provincia', attribute='Provincia')
    altura = fields.Field(column_name='Altura', attribute='altura')
    
    class Meta:
        model = Sitio
        fields = ()
        export_order = (
            'sitio',
            'entel_id',
            'nombre',
            'comuna',
            'provincia',
            'altura',
            'lat_base',
            'lon_base',
        )
        import_id_fields = ('entel_id',)

@admin.register(Sitio)
class SitioAdmin(ImportExportModelAdmin):
    resource_class = SitiosResource
    list_display = (
        'PTICellID',
        'EntelID',
        'nombre_modificado',
        'altura',
        'lat_nombre',
        'lon_nombre',
    )

    def nombre_modificado(self, obj):
        """
        Método para modificar el valor de 'Nombre', mostrando solo la parte después del '-'.
        """
        # Dividir el nombre por '-' y tomar el último elemento
        partes = obj.Nombre.split('-')
        return partes[-1] if partes else obj.Nombre
    nombre_modificado.short_description = 'Nombre'
    
    def lat_nombre(self, obj):
        return obj.lat_base
    lat_nombre.short_description = 'Latitud Base'
    
    def lon_nombre(self, obj):
        return obj.lon_base
    lon_nombre.short_description = 'Longitud Base'

    

class FormularioTXResource(resources.ModelResource):
    etapa = fields.Field(column_name='Etapa', attribute='etapa')
    usuario = fields.Field(
        column_name='ITO',
        attribute='usuario',
        widget=ForeignKeyWidget(User, 'username'))
    sitio = fields.Field(
        column_name='PTI Cell ID',
        attribute='sitio',
        widget=ForeignKeyWidget(Sitio, 'PTICellID'))
    entel_id = fields.Field(column_name='ID Entel', attribute='entel_id')
    nombre = fields.Field(column_name='Nombre', attribute='nombre')
    comuna = fields.Field(column_name='Comuna', attribute='comuna')
    provincia = fields.Field(column_name='Provincia', attribute='provincia')
    dim = fields.Field(column_name='Dimensiones', attribute='dimensiones')
    des = fields.Field(column_name='Deslindes', attribute='deslindes')
    aSitio = fields.Field(column_name='Acceso al Sitio', attribute='accesoSitio')
    aSitioCons = fields.Field(column_name='Acceso para Construcción', attribute='accesoSitioConstruccion')
    lAcceso = fields.Field(column_name='Longitud Acceso', attribute='longitudAcceso')
    lAccesoCons = fields.Field(column_name='Longitud Acceso Construcción', attribute='longitudAccesoConstuccion')
    tSuelo = fields.Field(column_name='Tipo de Suelo', attribute='tipoSuelo')
    obst = fields.Field(column_name='Obstáculos', attribute='obstaculos')
    adi = fields.Field(column_name='Adicionales', attribute='adicionales')
    pEnergia = fields.Field(column_name='Proveedor de Energía', attribute='proveedorEnergia')
    cEnergia = fields.Field(column_name='Capacidad de Energía', attribute='capacidadEnergia')
    lat = fields.Field(column_name='Latitud', attribute='lat')
    lon = fields.Field(column_name='Longitud', attribute='lon')
    latE = fields.Field(column_name='Latitud Empalme', attribute='lat_energia')
    lonE = fields.Field(column_name='Longitud Empalme', attribute='lon_energia')
    dist_empalme_inspeccion = fields.Field(column_name='Distancia al Empalme', attribute='distanciaEmpalmeSitio')

    lat_I = fields.Field(column_name='Latitud_base', attribute='lat_base')
    lon_I = fields.Field(column_name='Longitud_base', attribute='lon_base')

    dist_base_inspeccion = fields.Field(column_name='Distancia Inmobiliaria/Mandato a Inspeccion', attribute='dist_base_inspeccion')

    comentarios = fields.Field(column_name='Comentarios', attribute='comentario')
    
    altura = fields.Field(column_name='Altura', attribute='altura')
    
    fecha_creacion = fields.Field(column_name='Fecha Creación', attribute='fecha_creacion')

    class Meta:
        model = FormularioTX
        fields = ()
        export_order = (
            'etapa',
            'sitio',
            'entel_id',
            'nombre',
            'comuna',
            'provincia',
            'usuario',
            'altura',
            'dim',
            'des',
            'aSitio',
            'aSitioCons',
            'lAcceso',
            'lAccesoCons',
            'tSuelo',
            'obst',
            'adi',
            'pEnergia',
            'cEnergia',
            'lat',
            'lon',
            'latE',
            'lonE',
            'dist_empalme_inspeccion',
            'lat_I',
            'lon_I',
            'dist_base_inspeccion',
            'comentarios',
            'fecha_creacion',
        )
        import_id_fields = ('entel_id',)

@admin.register(FormularioTX)
class FormularioTXAdmin(ImportExportModelAdmin):
    resource_class = FormularioTXResource
    list_display = (
        'sitio',
        'entel_id',
        'usuario',
        'etapa',
        'dist_base_inspeccion_display',
        'related_images_display_small', 
    )
    list_editable = (
        'etapa',
    )
    
    readonly_fields = (
        'imagen_thumb', 
        'lat_gms', 
        'lon_gms',
        'lat_base_gms',
        'lon_base_gms',
        'lat_energia_gms',
        'lon_energia_gms',
        'imagen_deslindes_display',
        'entel_id',
        'nombre',
        'comuna',
        'provincia',
        'related_images_display_small',
        'related_images_display'
        )

    def dist_base_inspeccion_display(self, obj):
        # Aquí puedes retornar lo que originalmente se mostraría en "dist_base_inspeccion"
        return obj.dist_base_inspeccion
    dist_base_inspeccion_display.short_description = 'Desfase' 
    
    def imagen_thumb(self, obj):
        if obj.imagen:  # Reemplaza 'imagen' con el nombre real de tu campo de imagen en el modelo FormularioPreIng
            return format_html('<img src="{}" width="620" height=""/>', obj.imagen.url)
        return "No hay imagen"
    imagen_thumb.short_description = 'Vista Previa de la Imagen'
    
    def imagen_deslindes_display(self, obj):
        if obj.imagen_deslindes():
            return format_html('<img src="{}" width="350" height="auto" />', obj.imagen_deslindes())
        return "No Image"
    imagen_deslindes_display.short_description = 'Esquema Ejemplo: 18/18/+50/+100'

    def get_readonly_fields(self, request, obj=None):
        # Aquí puedes añadir lógica adicional si necesitas
        return self.readonly_fields


    def related_images_display_small(self, obj):
        # Este método busca imágenes relacionadas en la otra aplicación
        related_images = Image.objects.filter(etapa=obj.etapa, sitio=obj.sitio)
        if related_images.exists():
            return format_html(''.join([f'<img src="{img.pic.url}" width="50" height="auto" style="margin-right: 10px;"/>' for img in related_images]))
        return "No hay imágenes relacionadas"
    related_images_display_small.short_description = 'Imágenes Relacionadas'

    def related_images_display(self, obj):
        # Este método busca imágenes relacionadas en la otra aplicación
        related_images = Image.objects.filter(etapa=obj.etapa, sitio=obj.sitio)
        if related_images.exists():
            html_content = ['<div class="grid-container">']
            for img in related_images:
                image_html = f'<div class="grid-item"> <img src="{img.pic.url}" width="100%" height="auto" style="text-align: center; display: flex; flex-direction: column; align-items: center;"/>'
                description_html = f'<p style="margin-right: 60px;">{img.descripcion}</p></div>' if img.descripcion else '</div>'
                html_content.append(image_html)
                html_content.append(description_html) 
            html_content.append('</div>')
            return format_html(''.join(html_content))
        return "No hay imágenes relacionadas"
    related_images_display.short_description = 'Imágenes Relacionadas'

    def lat_gms(self, obj):
        return dec_to_gms(obj.lat, is_lat=True)
    lat_gms.short_description = "Latitud (GMS)"

    def lon_gms(self, obj):
        return dec_to_gms(obj.lon, is_lat=False)
    lon_gms.short_description = "Longitud (GMS)"

    def lat_base_gms(self, obj):
        return dec_to_gms(obj.lat_base, is_lat=True)
    lat_base_gms.short_description = "Latitud (GMS)"

    def lon_base_gms(self, obj):
        return dec_to_gms(obj.lon_base, is_lat=False)
    lon_base_gms.short_description = "Logitud (GMS)"
    
    def lat_energia_gms(self, obj):
        return dec_to_gms(obj.lat_energia, is_lat=True)
    lat_energia_gms.short_description = "Latitud (GMS)"
    
    def lon_energia_gms(self, obj):
        return dec_to_gms(obj.lon_energia, is_lat=False)
    lon_energia_gms.short_description = "Logitud (GMS)"

        # Ajustando la disposición de los campos usando fieldsets
    fieldsets = (
        ('Información General', {  # Ajusta los títulos y campos según necesites
            'fields': (
                'dist_base_inspeccion',
                ('sitio','entel_id', 'etapa'), 
                'nombre', 
                ('comuna','provincia', 'altura'), 
                ),
        }),
        ('Datos Geograficos', {  # Este es el título de la sección
            'fields': (
                'imagen_thumb',
                ('lat','lat_gms'),
                ('lon','lon_gms'),
                ('lat_base', 'lat_base_gms'),
                ('lon_base', 'lon_base_gms'),
                ('lat_energia', 'lat_energia_gms'),
                ('lon_energia', 'lon_energia_gms'),
                'distanciaEmpalmeSitio',
                'comentario'
                ),
            'description': 'Mandato/Inmobiliaria "M", Inspeccion "I", Empalme',
        }),

        ('Datos Constructivos', {  # Este es el título de la sección
            'fields': (
                'dimensiones',
                'imagen_deslindes_display',
                'deslindes',
                'accesoSitio',
                'accesoSitioConstruccion',
                'longitudAcceso',
                'longitudAccesoConstuccion',
                'tipoSuelo',
                'obstaculos',
                'adicionales',
                'proveedorEnergia',
                ),
        }),
        ('Reporte fotografico', {  # Este es el título de la sección
            'fields': (
                'related_images_display',
                ),
        }),


        ('Registro', {  # Este es el título de la sección
            'fields': (
                'fecha_creacion',
                'usuario',
                'imagen' 
                ),
        }),

    )


