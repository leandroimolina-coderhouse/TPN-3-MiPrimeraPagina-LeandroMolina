from django.shortcuts import render
from .forms import MarcaForm, AutoForm, ClienteForm, BuscarAutoForm
from .models import Auto

def inicio(request):
    return render(request, "autos/inicio.html")


def crear_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "autos/formulario.html", {"form": form, "titulo": "Alta de Marca"})


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


