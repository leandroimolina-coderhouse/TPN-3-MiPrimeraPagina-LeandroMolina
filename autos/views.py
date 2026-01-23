from django.shortcuts import render
from .forms import MarcaForm, AutoForm, ClienteForm, BuscarAutoForm
from .models import Auto, Marca

def inicio(request):
    return render(request, "autos/inicio.html")

def acerca_de(request):
    return render(request, "autos/acerca_de.html")


def crear_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "autos/formulario.html", {"form": form, "titulo": "Alta de Marca"})

def ver_marca(request):
    marcas = Marca.objects.first()
    return render(request, 'autos/ver_marca.html', {'marcas': marcas})


def crear_auto(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "autos/formulario.html", {"form": form, "titulo": "Alta de Auto"})


def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "autos/formulario.html", {"form": form, "titulo": "Alta de Cliente"})


def buscar_auto(request):
    form = BuscarAutoForm(request.GET or None)
    autos = []

    if form.is_valid():
        modelo = form.cleaned_data.get("modelo")
        autos = Auto.objects.filter(modelo__icontains=modelo)

    return render(request, "autos/buscar.html", {"form": form, "autos": autos})


