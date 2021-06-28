from django.urls import path
from .views import index, stock, listaReparacion, historialReparacion, registrarVenta
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('stock', stock, name="stock"),
    path('listaReparacion', listaReparacion, name="listaReparacion"),
    path('historialReparacion', historialReparacion, name="historialReparacion"),
    path('registrarVenta', registrarVenta, name="registrarVenta"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
]