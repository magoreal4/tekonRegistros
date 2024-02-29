from django.contrib import admin
from .models import FormularioTX, FormularioPreIng, Sitio, User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

  
class SitiosResource(resources.ModelResource):
    sitio = fields.Field(column_name='PTI Cell ID',attribute='PTICellID',)
    entel_id = fields.Field(column_name='ID Entel', attribute='EntelID')
    nombre = fields.Field(column_name='Nombre', attribute='Nombre')
    comuna = fields.Field(column_name='Comuna', attribute='Comuna')
    provincia = fields.Field(column_name='Provincia', attribute='Provincia')

    lat_nominal = fields.Field(column_name='Lat Nominal', attribute='lat_nominal')
    lon_nominal = fields.Field(column_name='Lon Nominal', attribute='lon_nominal')
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
            'lat_nominal', 
            'lon_nominal', 
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
        'lat_nominal',
        'lon_nominal',
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
    
    lat_N = fields.Field(column_name='Latitud Nominal', attribute='lat_nominal')
    lon_N = fields.Field(column_name='Longitud Nominal', attribute='lon_nominal')
    lat_I = fields.Field(column_name='Latitud Inmobiliaria', attribute='lat_inmobiliaria')
    lon_I = fields.Field(column_name='Longitud Inmobiliaria', attribute='lon_inmobiliaria')

    dist_nominal_inmobiliaria = fields.Field(column_name='Distancia Nominal a Inmobiliaria', attribute='dist_nominal_inmobiliaria')
    dist_nominal_inspeccion = fields.Field(column_name='Distancia Nominal a Inspeccion', attribute='dist_nominal_inspeccion')
    dist_inmobiliaria_inspeccion = fields.Field(column_name='Distancia Inmobiliaria a Inspeccion', attribute='dist_inmobiliaria_inspeccion')
    
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
            'lat_N', 
            'lon_N', 
            'lat_I', 
            'lon_I',
            'dist_nominal_inmobiliaria',
            'dist_nominal_inspeccion',
            'dist_inmobiliaria_inspeccion',
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
        'dist_nominal_inmobiliaria',
        'dist_nominal_inspeccion',
        'dist_inmobiliaria_inspeccion',
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
    
    lat_M = fields.Field(column_name='Latitud Nominal', attribute='lat_mandato')
    lon_M = fields.Field(column_name='Longitud Nominal', attribute='lon_mandato')

    dist_mandato_ingenieria = fields.Field(column_name='Distancia Mandato a Ingenieria', attribute='dist_mandato_ingenieria')
   
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

    )
