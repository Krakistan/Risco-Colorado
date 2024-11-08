from django.shortcuts import redirect, render
from .forms import Inicio, Registrarse, Cotizacion



def home(request):
    inicio_form = Inicio(request.POST or None)
    cotizacion_form = Cotizacion(request.POST or None)

    if request.method == 'POST':
        if 'inicio-form' in request.POST:
            if inicio_form.is_valid():
                inicio_form.save()
                return render(request, 'home.html', {'inicio_form': inicio_form})

        elif 'cotizacion-form' in request.POST:
            if cotizacion_form.is_valid():
                cotizacion_form.save()
                return render(request, 'home.html', {'cotizacion_form': cotizacion_form})

    context = {
        'inicio_form': inicio_form,
        'cotizacion_form': cotizacion_form,
    }
    return render(request, 'home.html', context)

def registrarse(request):
    if request.method == 'POST':
        registrarse_form = Registrarse(request.POST)
        if registrarse_form.is_valid():
            registrarse_form.save()
            return redirect('home.html')
    else:
        registrarse_form = Registrarse()

    context = {
        'registrarse_form': registrarse_form,
    }
    return render(request, 'registrarse.html', context)