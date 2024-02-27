from django.contrib import admin
from .models import Formulario1, Sitio, User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

class Formulario1Resource(resources.ModelResource):
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
    lat = fields.Field(column_name='Latitud', attribute='lat')
    lon = fields.Field(column_name='Longitud', attribute='lon')
    dim = fields.Field(column_name='Dimensiones', attribute='dimensiones')
    des = fields.Field(column_name='Deslindes', attribute='deslindes')
    aSitio = fields.Field(column_name='Acceso al Sitio', attribute='accesoSitio')
    aSitioCons = fields.Field(column_name='Acceso para Construcción', attribute='accesoSitioConstruccion')
    lAcceso = fields.Field(column_name='Longitud Acceso', attribute='longitudAcceso')
    lAccesoCons = fields.Field(column_name='Longitud Acceso Construcción', attribute='longitudAccesoConstruccion')
    tSuelo = fields.Field(column_name='Tipo de Suelo', attribute='tipoSuelo')
    obst = fields.Field(column_name='Obstáculos', attribute='obstaculos')
    adi = fields.Field(column_name='Adicionales', attribute='adicionales')
    pEnergia = fields.Field(column_name='Proveedor de Energía', attribute='proveedorEnergia')
    latE = fields.Field(column_name='Latitud Empalme', attribute='latEnergia')
    lonE = fields.Field(column_name='Longitud Empalme', attribute='lonEnergia')
    cEnergia = fields.Field(column_name='Capacidad de Energía', attribute='capacidadEnergia')
    dEmpalmeSitio = fields.Field(column_name='Distancia al Empalme', attribute='distanciaEmpalmeSitio')
    class Meta:
        model = Formulario1
        fields = ()
        export_order = (
            'sitio', 
            'entel_id', 
            'nombre', 
            'comuna', 
            'provincia', 
            'usuario',  
            'lat', 
            'lon', 
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
            'latE', 
            'lonE', 
            'cEnergia', 
            'dEmpalmeSitio'
        )
        import_id_fields = ('entel_id',)
        
@admin.register(Formulario1)
class Formulario1Admin(ImportExportModelAdmin):
    resource_class = Formulario1Resource
    list_display = (
        'sitio',
        'entel_id',
        'usuario',
        'nombre',
        'comuna',
        'provincia',
        'lat', 
        'lon',  
        'distanciaEmpalmeSitio', 
    )

  
class SitiosResource(resources.ModelResource):
    sitio = fields.Field(column_name='PTI Cell ID',attribute='PTICellID',)
    entel_id = fields.Field(column_name='ID Entel', attribute='EntelID')
    nombre = fields.Field(column_name='Nombre', attribute='Nombre')
    comuna = fields.Field(column_name='Comuna', attribute='Comuna')
    provincia = fields.Field(column_name='Provincia', attribute='Provincia')
    class Meta:
        model = Sitio
        fields = ()
        export_order = (
            'sitio', 
            'entel_id', 
            'nombre', 
            'comuna', 
            'provincia', 
        )
        import_id_fields = ('entel_id',)
        
@admin.register(Sitio)
class SitioAdmin(ImportExportModelAdmin):
    resource_class = SitiosResource
    list_display = (
        'PTICellID',
        'EntelID',
        'Nombre',
        'Comuna',
        'Provincia'
    )