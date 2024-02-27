from django import forms
from .models import Formulario1, Sitio

class Formulario1Form(forms.ModelForm):
    sitio = forms.ModelChoiceField(queryset=Sitio.objects.all(), empty_label="Seleccione un Sitio")

    class Meta:
        model = Formulario1
        # Incluyendo todos los campos del modelo Formulario1
        fields = ['sitio', 
                  'lat', 
                  'lon', 
                  'dimensiones', 
                  'deslindes', 
                  'accesoSitio',
                  'accesoSitioConstruccion',
                  'longitudAcceso', 
                  'longitudAccesoConstuccion',
                  'tipoSuelo',
                  'obstaculos',
                  'adicionales',
                  'proveedorEnergia',
                  'latEnergia', 
                  'lonEnergia',
                  'capacidadEnergia', 
                  ]

    def __init__(self, *args, **kwargs):
        super(Formulario1Form, self).__init__(*args, **kwargs)
        
        # Configuraciones de campos personalizadas
        self.fields['sitio'].label = "Codigo Sitio PTI:"
        self.fields['lat'].label = "Latitud:"
        self.fields['lon'].label = "Longitud:"
        self.fields['deslindes'].label = "Deslindes:"
        self.fields['accesoSitio'].label = "Acceso al Sitio (Huella):"
        self.fields['accesoSitioConstruccion'].label = "Acceso al Sitio para Construcción:"
        self.fields['longitudAcceso'].label = "Longitud acceso al Sitio (m):"
        self.fields['longitudAccesoConstuccion'].label = "Longitud acceso para construccion (m):"
        self.fields['tipoSuelo'].label = "Tipo de Suelo del sitio y huella:"
        self.fields['obstaculos'].label = "Edificaciones cercanas/obstaculos:"
        self.fields['adicionales'].label = "Trabajos adicionales a considerar:"
        self.fields['proveedorEnergia'].label = "Proveedor de Energia:"
        self.fields['latEnergia'].label = "Latitud:"
        self.fields['lonEnergia'].label = "Longitud:"
        self.fields['capacidadEnergia'].label = "Capacidad de Energia:"

                
        # # Placeholders y Helpers para los nuevos campos
        self.fields['lat'].widget.attrs.update({'placeholder': 'Ej: -33.456789'})
        self.fields['lat'].help_text = 'Ubiquese en el punto del eje de la estructura y presione el boton de arriba.'
        self.fields['lon'].widget.attrs.update({'placeholder': 'Ej: -70.123456'})
        self.fields['dimensiones'].widget.attrs.update({'placeholder': 'Ej: 10x20 m.'})
        self.fields['deslindes'].widget.attrs.update({'placeholder': 'Ej: 18 / 18 / +50 / +100 m'})
        self.fields['deslindes'].help_text = 'Distancia a los bordes de la propiedad, las distancias cortas deben ser precisas.'
        self.fields['accesoSitio'].help_text = 'Describir el acceso, si se requiere mejora, movimiento de tierras, rellenos, alcantarillado, otros.'
        # self.fields['accesoSitio'].widget = forms.Textarea()  # Cambiamos el widget a Textarea
        self.fields['accesoSitio'].widget.attrs.update({'rows': '3'})
        self.fields['accesoSitioConstruccion'].help_text = 'Verificar acceso para construcción. Ingreso grúa, camion hormigonero.'
        self.fields['accesoSitioConstruccion'].widget.attrs.update({'rows': '4'})
        self.fields['longitudAcceso'].widget.attrs.update({'placeholder': 'Ej: 100'})
        self.fields['longitudAcceso'].help_text = 'Longitud de la huellas en el sitio.'
        self.fields['longitudAccesoConstuccion'].widget.attrs.update({'placeholder': 'Ej: 100'})
        self.fields['longitudAccesoConstuccion'].help_text = 'Longitud de acceso a construcción (generalmente idem a la huella).'
        self.fields['tipoSuelo'].help_text = 'Tipo de suelo, sembradillos, zona anegada, suelo consolidado, se debe hacer desbroce, etc.'
        self.fields['tipoSuelo'].widget.attrs.update({'rows': '3'})
        self.fields['obstaculos'].help_text = 'Verificar si existen obstaculos, tanto para el montaje como para la consturrción'
        self.fields['obstaculos'].widget.attrs.update({'rows': '2'})
        self.fields['adicionales'].help_text = 'Trabajos como: linea electrica subterranea, alcantarilla, porton, etc.'
        self.fields['adicionales'].widget.attrs.update({'rows': '2'})
        self.fields['latEnergia'].widget.attrs.update({'placeholder': 'Ej: -33.456789'})
        self.fields['latEnergia'].help_text = 'Ubiquese en el punto de empalme y presione el boton de arriba.'
        self.fields['lonEnergia'].widget.attrs.update({'placeholder': 'Ej: -70.123456'})
        self.fields['capacidadEnergia'].widget.attrs.update({'placeholder': 'Ej: 25 A'})