from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('acerca-de', acerca_de, name='acerca_de'),
    path('crear-marca/', crear_marca, name='crear_marca'),
    path('ver-marca/', ver_marca, name='ver_marca'),
    path('crear-auto/', crear_auto, name='crear_auto'),
    path('crear-cliente/', crear_cliente, name='crear_cliente'),
    path('buscar-auto/', buscar_auto, name='buscar_auto'),
]
