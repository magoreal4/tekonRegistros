from django.shortcuts import render, redirect
from .forms import ImagesForm
from .models import Image
from formularios.models import Sitio

# Create your views here.
def listar(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, "imagenes/lista_imagenes.html", context)

def fileupload(request):
    form = ImagesForm(request.POST, request.FILES)
    if request.method == 'POST':
        images = request.FILES.getlist('pic')
        sitio_id = request.POST.get('sitio')
        sitio_obj = Sitio.objects.get(id=sitio_id)
        etapa = request.POST.get('etapa')
        for image in images:
            image_ins = Image(pic = image, sitio = sitio_obj, etapa = etapa)
            image_ins.save()
        return redirect('imagenes:lista_imagenes')
    context = {'form': form}
    return render(request, "imagenes/subir_imagen.html", context)