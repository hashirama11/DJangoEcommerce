from django.shortcuts import render
from . models import Categoria, Productos

# Create your views here.

"""Vistas para el catalogo de productos"""

def index(request):
    listaProductos = Productos.objects.all()
    context = {
        'productos': listaProductos
    }
    return render(request, 'index.html', context)

