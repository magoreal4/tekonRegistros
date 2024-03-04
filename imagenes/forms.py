
from formularios.models import Sitio

from django import forms
from .models import Image

class ImagesForm(forms.ModelForm):
    pic = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }), label = "")
    sitio = forms.ModelChoiceField(queryset = Sitio.objects.all(), label = "Sitio")
    
    class Meta:
        model = Image
        fields = ['pic', 'sitio', 'etapa']