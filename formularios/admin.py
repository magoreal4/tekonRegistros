from django.contrib import admin
from .models import FormularioTX, FormularioPreIng, Sitio, User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.utils.html import format_html


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

    lat_inmobiliaria = fields.Field(column_name='Lat Inmobiliaria', attribute='lat_inmobiliaria')
    lon_inmobiliaria = fields.Field(column_name='Lon Inmobiliaria', attribute='lon_inmobiliaria')
    lat_mandato = fields.Field(column_name='Lat Mandato', attribute='lat_mandato')
    lon_mandato = fields.Field(column_name='Lon Mandato', attribute='lon_mandato')


    class Meta:
        model = Sitio
        fields = ()
        export_order = (
            'sitio',
            'entel_id',
            'nombre',
            'comuna',
            'provincia',
            'lat_inmobiliaria',
            'lon_inmobiliaria',
            'lat_mandato',
            'lon_mandato'
        )
        import_id_fields = ('entel_id',)

@admin.register(Sitio)
class SitioAdmin(ImportExportModelAdmin):
    resource_class = SitiosResource
    list_display = (
        'PTICellID',
        'EntelID',
        'nombre_modificado',
        'lat_inmobiliaria',
        'lon_inmobiliaria',
        'lat_mandato',
        'lon_mandato',
    )
    list_editable = (
        'lat_inmobiliaria',
        'lon_inmobiliaria',
        'lat_mandato',
        'lon_mandato',
    )
    def nombre_modificado(self, obj):
        """
        Método para modificar el valor de 'Nombre', mostrando solo la parte después del '-'.
        """
        # Dividir el nombre por '-' y tomar el último elemento
        partes = obj.Nombre.split('-')
        return partes[-1] if partes else obj.Nombre

    nombre_modificado.short_description = 'Nombre'


class FormularioTXResource(resources.ModelResource):
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


    lat_I = fields.Field(column_name='Latitud Inmobiliaria', attribute='lat_inmobiliaria')
    lon_I = fields.Field(column_name='Longitud Inmobiliaria', attribute='lon_inmobiliaria')

    dist_inmobiliaria_inspeccion = fields.Field(column_name='Distancia Inmobiliaria a Inspeccion', attribute='dist_inmobiliaria_inspeccion')

    comentarios = fields.Field(column_name='Comentarios', attribute='comentario')

    class Meta:
        model = FormularioTX
        fields = ()
        export_order = (
            'sitio',
            'entel_id',
            'nombre',
            'comuna',
            'provincia',
            'usuario',
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
            'dist_inmobiliaria_inspeccion',
            'comentarios'
        )
        import_id_fields = ('entel_id',)

@admin.register(FormularioTX)
class FormularioTXAdmin(ImportExportModelAdmin):
    resource_class = FormularioTXResource
    list_display = (
        'sitio',
        'entel_id',
        'usuario',
        'nombre',
        'lat',
        'lon',
        'distanciaEmpalmeSitio',
        'dist_inmobiliaria_inspeccion',
        'imagen',
    )
    
    readonly_fields = (
        'imagen_thumb', 
        'lat_gms', 
        'lon_gms',
        'lat_inmobiliaria_gms',
        'lon_inmobiliaria_gms',
        'lat_energia_gms',
        'lon_energia_gms',
        'imagen_deslindes_display',
        )

    def imagen_thumb(self, obj):
        if obj.imagen:  # Reemplaza 'imagen' con el nombre real de tu campo de imagen en el modelo FormularioPreIng
            return format_html('<img src="{}" width="480" height="300"/>', obj.imagen.url)
        return "No hay imagen"
    imagen_thumb.short_description = 'Vista Previa de la Imagen'
    
    def imagen_deslindes_display(self, obj):
        if obj.imagen_deslindes():
            return format_html('<img src="{}" width="350" height="auto" />', obj.imagen_deslindes())
        return "No Image"
    imagen_deslindes_display.short_description = 'Esquema 18/18/+50/+100'

    def get_readonly_fields(self, request, obj=None):
        # Aquí puedes añadir lógica adicional si necesitas
        return self.readonly_fields


    def lat_gms(self, obj):
        return dec_to_gms(obj.lat, is_lat=True)
    lat_gms.short_description = "Latitud (GMS)"

    def lon_gms(self, obj):
        return dec_to_gms(obj.lon, is_lat=False)
    lon_gms.short_description = "Longitud (GMS)"

    def lat_inmobiliaria_gms(self, obj):
        return dec_to_gms(obj.lat_inmobiliaria, is_lat=False)
    lat_inmobiliaria_gms.short_description = "Latitud (GMS)"

    def lon_inmobiliaria_gms(self, obj):
        return dec_to_gms(obj.lon_inmobiliaria, is_lat=False)
    lon_inmobiliaria_gms.short_description = "Logitud (GMS)"
    
    def lat_energia_gms(self, obj):
        return dec_to_gms(obj.lat_energia, is_lat=False)
    lat_energia_gms.short_description = "Latitud (GMS)"
    
    def lon_energia_gms(self, obj):
        return dec_to_gms(obj.lon_energia, is_lat=False)
    lon_energia_gms.short_description = "Logitud (GMS)"

        # Ajustando la disposición de los campos usando fieldsets
    fieldsets = (
        ('Información General', {  # Ajusta los títulos y campos según necesites
            'fields': ('sitio', 'entel_id', 'usuario', 'nombre', 'comuna', 'provincia',),
        }),
        ('Datos Geograficos', {  # Este es el título de la sección
            'fields': (
                'imagen_thumb',
                ('lat','lat_gms'),
                ('lon','lon_gms'),
                ('lat_inmobiliaria', 'lat_inmobiliaria_gms'),
                ('lon_inmobiliaria', 'lon_inmobiliaria_gms'),
                'dist_inmobiliaria_inspeccion',
                ('lat_energia', 'lat_energia_gms'),
                ('lon_energia', 'lon_energia_gms'),
                'distanciaEmpalmeSitio',
                'comentario'
                ),
            'description': 'Coord.Inmobiliaria "M", Coord. Inspeccion "I"',
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
                'imagen'
                ),
        }),

    )


class FormularioPreIngResource(resources.ModelResource):
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

    lat_M = fields.Field(column_name='Latitud Mandato/Inmobiliaria', attribute='lat_mandato')
    lon_M = fields.Field(column_name='Longitud Mandato/Inmobiliaria', attribute='lon_mandato')

    dist_mandato_ingenieria = fields.Field(column_name='Distancia Inspeccion a Mandato/Inmobiliaria', attribute='dist_mandato_ingenieria')

    comentarios = fields.Field(column_name='Comentarios', attribute='comentario')




    class Meta:
        model = FormularioPreIng
        fields = ()

        export_order = (
            'sitio',
            'entel_id',
            'nombre',
            'comuna',
            'provincia',
            'usuario',
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
            'lat_M',
            'lon_M',
            'dist_mandato_ingenieria',
            'comentarios'
        )
        import_id_fields = ('entel_id',)

@admin.register(FormularioPreIng)
class FormularioPreIngAdmin(ImportExportModelAdmin):
    resource_class = FormularioPreIngResource
    list_display = (
        'sitio',
        'entel_id',
        'usuario',
        'nombre',
        'lat',
        'lon',
        'distanciaEmpalmeSitio',
        'dist_mandato_ingenieria',
        'imagen',
        

    )

    readonly_fields = (
        'imagen_thumb', 
        'lat_gms', 
        'lon_gms',
        'lat_mandato_gms',
        'lon_mandato_gms',
        'lat_energia_gms',
        'lon_energia_gms',
        'imagen_deslindes_display',
        
        )

    def imagen_thumb(self, obj):
        if obj.imagen:  # Reemplaza 'imagen' con el nombre real de tu campo de imagen en el modelo FormularioPreIng
            return format_html('<img src="{}" width="480" height="300"/>', obj.imagen.url)
        return "No hay imagen"
    imagen_thumb.short_description = 'Vista Previa de la Imagen'
    
    def imagen_deslindes_display(self, obj):
        if obj.imagen_deslindes():
            return format_html('<img src="{}" width="350" height="auto" />', obj.imagen_deslindes())
        return "No Image"
    imagen_deslindes_display.short_description = 'Esquema 18/18/+50/+100'

    def get_readonly_fields(self, request, obj=None):
        # Aquí puedes añadir lógica adicional si necesitas
        return self.readonly_fields


    def lat_gms(self, obj):
        return dec_to_gms(obj.lat, is_lat=True)
    lat_gms.short_description = "Latitud (GMS)"

    def lon_gms(self, obj):
        return dec_to_gms(obj.lon, is_lat=False)
    lon_gms.short_description = "Longitud (GMS)"

    def lat_mandato_gms(self, obj):
        return dec_to_gms(obj.lat_mandato, is_lat=False)
    lat_mandato_gms.short_description = "Latitud (GMS)"

    def lon_mandato_gms(self, obj):
        return dec_to_gms(obj.lon_mandato, is_lat=False)
    lon_mandato_gms.short_description = "Logitud (GMS)"
    
    def lat_energia_gms(self, obj):
        return dec_to_gms(obj.lat_energia, is_lat=False)
    lat_energia_gms.short_description = "Latitud (GMS)"
    
    def lon_energia_gms(self, obj):
        return dec_to_gms(obj.lon_energia, is_lat=False)
    lon_energia_gms.short_description = "Logitud (GMS)"



        # Ajustando la disposición de los campos usando fieldsets
    fieldsets = (
        ('Información General', {  # Ajusta los títulos y campos según necesites
            'fields': ('sitio', 'entel_id', 'usuario', 'nombre', 'comuna', 'provincia',),
        }),
        ('Datos Geograficos', {  # Este es el título de la sección
            'fields': (
                'imagen_thumb',
                ('lat','lat_gms'),
                ('lon','lon_gms'),
                ('lat_mandato', 'lat_mandato_gms'),
                ('lon_mandato', 'lon_mandato_gms'),
                'dist_mandato_ingenieria',
                ('lat_energia', 'lat_energia_gms'),
                ('lon_energia', 'lon_energia_gms'),
                'distanciaEmpalmeSitio',
                'comentario'
                ),
            'description': 'Coord. Mandato/Inmobiliaria "M", Coord. Inspeccion "I"',
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
                'imagen'
                ),
        }),

    )
