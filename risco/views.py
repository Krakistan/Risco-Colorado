from datetime import date
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from .models import Productos,Compra, ProductosCompra
from .forms import CotizacionForm, FormularioRegistro
from django.contrib.auth import load_backend
from django.contrib.auth import login, authenticate



def home(request):
    productos_venta = Productos.objects.filter(tipo='Venta')
    productos_arriendo = Productos.objects.filter(tipo='Arriendo')

    
    context = {
        'productos_venta': productos_venta,
        'productos_arriendo': productos_arriendo,
        
    }    
    return render(request, 'risco/home.html', context)


def pagar(request):
    # URL de Webpay para pruebas
    webpay_url = "https://webpay3gint.transbank.cl/webpayserver/initTransaction"
    return redirect(webpay_url)


def carrito(request, indx=None):
    if 'carro' not in request.session:
        request.session['carro'] = []
    carro = request.session['carro']
    
    # Si se proporciona un índice, agregamos el producto al carrito
    if indx:
        producto = Productos.objects.filter(id=indx).first()
        if producto:
            carro.append({
                "id_producto": producto.id,
                "nombre": producto.nombre,
                "cantidad": 1,
                "precio": float(producto.precio),
                "imagen": producto.imagen.url if producto.imagen else None
            })
    
    # Calculamos el total teniendo en cuenta la cantidad de cada pr oducto
    total_precio = 0
    total_items = 0
    for c in carro:
        producto = Productos.objects.filter(id=c["id_producto"]).first()
        if producto:
            c["nombre"] = producto.nombre
            c["precio"] = float(producto.precio)
            c["imagen"] = producto.imagen.url if producto.imagen else None
            total_precio += c["precio"] * c["cantidad"]
            total_items += c["cantidad"]
        else:
            c["nombre"] = "Producto no disponible"
            c["precio"] = 0.0

    # Guardamos los cambios en la sesión
    request.session['carro'] = carro
    context = {
        'carrito': carro,
        'total_precio': total_precio,
        'total_items': total_items
    }
    return render(request, 'risco/carrito.html', context)








def anadir_al_carro(request, indx):
    if 'carro' not in request.session:
        request.session['carro'] = []

    carro_actual = request.session['carro']

    # Verificamos si el producto ya está en el carrito
    producto_existente = next((producto for producto in carro_actual if producto["id_producto"] == indx), None)

    if producto_existente:
        producto_existente["cantidad"] += 1
    else:
        producto = Productos.objects.filter(id=indx).first()
        if producto:
            carro_actual.append({
                "id_producto": producto.id,
                "nombre": producto.nombre,
                "cantidad": 1,
                "precio": float(producto.precio),
                "imagen": producto.imagen.url if producto.imagen else None
            })

    request.session['carro'] = carro_actual
    return redirect('carrito')


 

def eliminar_del_carro(request, indx):
    carro_actual = request.session['carro']
    carro_actual = [producto for producto in carro_actual if producto["id_producto"] != indx]
    request.session['carro'] = carro_actual
    return redirect('carrito')

def aumentar_cantidad(request, indx):
    carro_actual = request.session['carro']
    for producto in carro_actual:
        if producto["id_producto"] == indx:
            producto["cantidad"] += 1
    request.session['carro'] = carro_actual
    return redirect('carrito')

def disminuir_cantidad(request, indx):
    carro_actual = request.session['carro']
    for producto in carro_actual:
        if producto["id_producto"] == indx:
            producto["cantidad"] -= 1
            if producto["cantidad"] <= 0:
                carro_actual = [prod for prod in carro_actual if prod["id_producto"] != indx]
    request.session['carro'] = carro_actual
    return redirect('carrito')


def confirmar_compra(request):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para confirmar la compra")
        return redirect('iniciar_sesion')

    carro_actual = request.session.get('carro', [])
    if not carro_actual:
        messages.error(request, "No hay productos en el carrito")
        return redirect('carrito')

    compra = Compra(nombre_cliente=request.user.username, fecha=date.today())
    compra.save()

    for item in carro_actual:
        producto = get_object_or_404(Productos, id=item["id_producto"])
        ProductosCompra.objects.create(
            id_producto=producto,
            id_compra=compra,
            cantidad=item["cantidad"]
        )

    request.session['carro'] = []
    messages.success(request, "Compra confirmada con éxito")
    return redirect('home')




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