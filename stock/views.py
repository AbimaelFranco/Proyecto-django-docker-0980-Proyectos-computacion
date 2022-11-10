from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from carro.carro import Carro
from inventario.models import articulos
from usuarios.models import usuarios
from carro.carro import Carro


# Create your views here.

def home(request):

    carro = Carro(request)

    arts = articulos.objects.all()

    ultimos_articulos=[]
    #print("################################################")
    if len(arts)>3:
        for i in range(len(arts)-4, len(arts)):
            ultimos_articulos.append(arts[i])
    else:
        for i in range(0, len(arts)):
            ultimos_articulos.append(arts[i])
        #print(ultimos_articulos)
    #print("################################################")
    return render(request, "stock/home.html", {"arts":arts, "articulos":ultimos_articulos})
    #return render(request, "stock/home.html")

def carrito(request):

    return render(request, "stock/carrito.html")

def contacto(request):

    return render(request, "stock/contacto.html")

def manual_usuario(request):

    return render(request, "stock/manual_usuario.html")

def checkout(request):
    info_usuario = usuarios.objects.all()
    pedido_valido = True
    return render(request, "stock/checkout.html", {"info_usuario":info_usuario, "pedido_valido": pedido_valido})
    # return render(request, "stock/checkout.html", {"info_usuario":info_usuario})

def handle_not_found(request, exception):
    return render(request, "stock/error-page.html")