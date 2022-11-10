from django.shortcuts import render
from .carro import Carro

from inventario.models import articulos
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/autenticacion/iniciar_sesion")

def agregar_producto(request, producto_id):
    
    carro = Carro(request)

    producto = articulos.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("Carrito")


def eliminar_producto(request, producto_id):
    
    carro = Carro(request)

    producto = articulos.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Carrito")

def restar_producto(request, producto_id):
    
    carro = Carro(request)

    producto = articulos.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Carrito")

def limpiar_carro(request, producto_id):
    
    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("Carrito")