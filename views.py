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