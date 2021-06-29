from django.urls import path
from .views import index, stock, listaReparacion, historialReparacion, registrarVenta, solicitarReparacion, arriendoBicicleta, productos, reporteVentas, reporteServicios
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('stock', stock, name="stock"),
    path('listaReparacion', listaReparacion, name="listaReparacion"),
    path('historialReparacion', historialReparacion, name="historialReparacion"),
    path('registrarVenta', registrarVenta, name="registrarVenta"), 
    path('solicitarReparacion', solicitarReparacion, name="solicitarReparacion"), 
    path('arriendoBicicleta', arriendoBicicleta, name="arriendoBicicleta"), 
    path('productos', productos, name="productos"), 
    path('reporteVentas', reporteVentas, name="reporteVentas"), 
    path('reporteServicios', reporteServicios, name="reporteServicios"), 
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
]