from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Productos
from .forms import CotizacionForm, FormularioRegistro
from django.contrib.auth import load_backend



def home(request):
    productos_venta = Productos.objects.filter(tipo='Venta')
    productos_arriendo = Productos.objects.filter(tipo='Arriendo')
    
    context = {
        'productos_venta': productos_venta,
        'productos_arriendo': productos_arriendo
    }
    
    return render(request, 'risco/home.html', context)
def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            
            
            backend = load_backend('risco.backends.EmailBackend')
            usuario.backend = backend.__class__.__module__ + '.' + backend.__class__.__name__
            login(request, usuario)  
            
            return redirect('home')
    else:
        formulario = FormularioRegistro()
    return render(request, 'risco/registro.html', {'formulario': formulario})



def cotizacion(request):
    cotizacionform = CotizacionForm(request.POST or None)

    if request.method == 'POST':
        if cotizacionform.is_valid():
            cotizacionform.save()
            return redirect('home')  
        else:
            print(cotizacionform.errors)  

    return render(request, 'risco/cotizacion.html', {'cotizacionform': cotizacionform})



def nosotros(request):
    return render(request, 'risco/nosotros.html')