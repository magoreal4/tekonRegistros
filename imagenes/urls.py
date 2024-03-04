from django.urls import path
from . import views

app_name = 'imagenes'

urlpatterns = [
    path('listar/', views.listar, name='lista_imagenes'),
    path('subir/', views.fileupload, name='subir_imagen'), 
]
