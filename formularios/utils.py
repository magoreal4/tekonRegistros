# import requests
# from django.core.files.base import ContentFile
# from .models import FormularioPreIng

# def obtener_imagen_google_maps(latitud, longitud, sitio, zoom=13, maptype="hybrid", scale=2, tamano="640x400"):
#     base_url = "https://maps.googleapis.com/maps/api/staticmap?"
#     api_key = "AIzaSyD22EmbDEXIc7Meum5e2MCYj4D0JpDrmpUx"
    
#     params = {
#         "center": f"{latitud},{longitud}",
#         "zoom": zoom,
#         "size": tamano,
#         "maptype": maptype,  # "roadmap" Agrega este parámetro para obtener imágenes satelitales
#         "scale" : scale,
#         "key": api_key,
#         "markers": f"color:yellow|label:P|{latitud},{longitud}",  # Agrega un marcador rojo con la etiqueta 'A'
#     }
    
#     response = requests.get(base_url, params=params)
    
#     if response.status_code == 200:
#         imagen_mapa = FormularioPreIng(sitio=sitio)
#         imagen_mapa.imagen.save(f"{sitio}.png", ContentFile(response.content), save=True)
#         print(f"Imagen guardada como '{imagen_mapa.imagen.url}'")
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)
        
