from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def stock(request):
    return render(request, 'core/stock.html')

def listaReparacion(request):
    return render(request, 'core/listaReparacion.html')

def historialReparacion(request):
    return render(request, 'core/historialReparacion.html')

def registrarVenta(request):
    return render(request, 'core/registrarVenta.html')

def arriendoBicicleta(request):
    return render(request, 'core/arriendoBicicleta.html')

def solicitarReparacion(request):
    return render(request, 'core/solicitarReparacion.html')

def productos(request):
    return render(request, 'core/productos.html')

def reporteVentas(request):
    return render(request, 'core/reporteVentas.html')

def reporteServicios(request):
    return render(request, 'core/reporteServicios.html')

def reporteFabricacion(request):
    return render(request, 'core/reporteFabricacion.html')