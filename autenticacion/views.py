# from msilib.schema import ListView
from django.views.generic import ListView, View
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from autenticacion.utils import render_to_pdf
from .forms import CustomUserCreationForm  
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import itertools
from pedidos.models import Pedido
from pedidos.models import LineaPedido
from inventario.models import articulos
# from user.models import User
from django.contrib.auth.models import User
from usuarios.models import usuarios
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from axes.utils import reset
from usuarios.models import usuarios


from django.contrib.auth import get_user_model
User = get_user_model()

class VRegistro(View):

    def get(self, request):
        # form = UserCreationForm()
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form":form})

    def post(self, request):
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST, request.FILES)
        print(form)
        # nombre=form2.get_first_name()
        # print(nombre)

        if form.is_valid():
            usuario = form.save()
            # form.email_clean()
            # form.email_clean()
            ncui = form.cleaned_data.get('cui')
            # nimagen = form.cleaned_data.get('profile_imagen')
            img = form.cleaned_data.get("profile_imagen")
            # print(cui)
            # username=request.user.username
            # password=request.user.password1
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            usuario = authenticate(request=request, username=username, password=password)
            login(request, usuario)

            nuevo_usuario = usuarios(user=request.user, username=request.user.username, fisrt_name=request.user.first_name, last_name=request.user.last_name, email=request.user.email, cui=ncui, profile_image = img)
            nuevo_usuario.save()

            # messages.success(request,"Registro exitoso")

            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request, "registro/registro.html", {"form":form})



def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def iniciar_sesion(request):

    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario = authenticate(request=request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                reset(username=username)
                return redirect('Home')
            else:
                messages.error(request,"Usuario no válido")
        else:
            messages.error(request,"Información no válida")

    form = AuthenticationForm()
    return render(request, "login/login.html", {"form":form})


def perfil(request):

    articulos_comprados = LineaPedido.objects.all()
    pedidos_comprados = Pedido.objects.all()
    listado_todos_productos = articulos.objects.all()
    listado_usuarios = usuarios.objects.all()

    return render(request, "perfil/perfil.html", {"articulos_comprados":articulos_comprados, "listado_todos_productos":listado_todos_productos, 'listado_usuarios': listado_usuarios, 'pedidos_comprados': pedidos_comprados})

class perfil_pdf(View):
    # model= LineaPedido
    # template_name= "perfil/perfil.html"
    # context_object_name = 'articulos_comprados'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)    
    #     context['listado_todos_productos'] = articulos.objects.all()
    #     return context
    def get(self, request, *arg, **kwargs):
        user_id = request.user.id
        username = request.user.username
        email = request.user.email
        first_name = request.user.first_name
        last_name = request.user.last_name

        user={
            'id':user_id,
            'username': username,
            'first_name':first_name,
            'last_name': last_name,
            'email': email
        }

        print(user["username"])
        
        # articulos_comprados = LineaPedido.objects.get(user_id=user_id)
        articulos_comprados = LineaPedido.objects.all()
        listado_todos_productos = articulos.objects.all()
        pedidos_comprados = Pedido.objects.all()
        # print(articulos_comprados)

        articulos_comprados2=[]
        listado_todos_productos2=[]
        for articulos_comprados in articulos_comprados:
            # print(articulos_comprados.producto)
            if articulos_comprados.user_id == user_id:
                articulos_comprados2.append(articulos_comprados)
                articulo = articulos.objects.get(pk=articulos_comprados.producto_id)
                listado_todos_productos2.append(articulo)
        data={
            'articulos_comprados': articulos_comprados2,
            'listado_todos_productos': listado_todos_productos,
            'pedidos_comprados': pedidos_comprados,
            'user': user
        }
        pdf = render_to_pdf('perfil/perfil_pdf.html', data)
        # print(articulos_comprados2)
        
        return HttpResponse(pdf, content_type='application/pdf')


# def lockout(request, credentials, *args, **kwargs):
#     return JsonResponse({"status": "Mensaje de prueba"}, status=403)

def lockout(request, credentials, *args, **kwargs):
    for i in User.objects.all():
        # print(i.username)
        if i.username == credentials["username"]:
            correo_usuario = i.email
    # print("###########################################")
    # print(credentials["username"])
    # print("Correo: ", correo_usuario)
    # print("###########################################")
    try:
        enviar_mail(
            nombreusuario = credentials["username"],


            emailusuario = correo_usuario
        )
    except:
        print("No se ha podido enviar el correo")

    return render(request, "lockout/lockout.html")

def enviar_mail(**kwargs):

    asunto="Restablecimiento Contraseña en Kaori Shop"
    mensaje = render_to_string("emails/reset_pass.html",{

        "nombreusuario": kwargs.get("nombreusuario")

    })


    mensaje_texto=strip_tags(mensaje)
    from_email="correo@gmail.com"         ########Correo desde el que se envia        aajekdjonxyejtih 
    to=kwargs.get("emailusuario")               ########Correo desde al que se envia
    # to = "correo@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)