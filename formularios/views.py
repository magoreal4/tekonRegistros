from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Importa el decorador
from .forms import Formulario1Form


@login_required  # Asegura que solo usuarios logueados puedan acceder a esta vista
def formulario1_view(request):
    if request.method == 'POST':
        form = Formulario1Form(request.POST)
        if form.is_valid():
            # Crea una instancia del modelo, pero no la guarda todavía
            instancia = form.save(commit=False)
            # Asigna el usuario logueado a la instancia del modelo
            instancia.usuario = request.user
            # Ahora guarda la instancia del modelo en la base de datos
            instancia.save()
            # Si tu formulario tiene relaciones ManyToMany que necesiten guardarse, puedes hacerlo aquí:
            # form.save_m2m()
            return redirect('formularios:success')  # Redirige a una nueva URL en caso de éxito
    else:
        form = Formulario1Form()
    return render(request, 'formularios/formulario1.html', {'form': form})

# Añade esta nueva vista
def form_success(request):
    # Cambia '5' a la cantidad de segundos que desees antes de redirigir
    return render(request, 'formularios/success.html', {'redirect_time': 5})