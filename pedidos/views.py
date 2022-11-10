from email import message
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from usuarios.models import usuarios
from inventario.models import articulos



@login_required(login_url="/autenticacion/iniciar_sesion")

def procesar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido = pedido
        ))

    pedido_valido = True           #Si el pedido se invalida es false

    lineas_pedido2=lineas_pedido
    lineas_pedido3=lineas_pedido
    lineas_pedido4=lineas_pedido

    for lineas_pedido2 in lineas_pedido2:   #Confimarcion que el pedido sea valido
        # print("Nombre del producto: ", lineas_pedido2.producto, " Cantidad: ", lineas_pedido2.cantidad)
        en_stock = articulos.objects.get(pk=lineas_pedido2.producto_id)
        nueva_cantidad = en_stock.cantidad - lineas_pedido2.cantidad        
        
        if nueva_cantidad<0:
            pedido_valido = False
            break
        else:
            pedido_valido = True

    # print("El pedido es valido?: ", pedido_valido)

    if pedido_valido:
        for lineas_pedido3 in lineas_pedido3:   #Almacenamiento del pedido valido
            # print("Nombre del producto: ", lineas_pedido3.producto, " Cantidad: ", lineas_pedido3.cantidad)
            en_stock = articulos.objects.get(pk=lineas_pedido3.producto_id)
            nueva_cantidad = en_stock.cantidad - lineas_pedido3.cantidad        
            en_stock.cantidad=nueva_cantidad

            # if nueva_cantidad ==0:
            #     en_stock.disponibilidad =False

            en_stock.save()

        LineaPedido.objects.bulk_create(lineas_pedido)

        info_usuario = usuarios.objects.all()

        # for lineas_pedido4 in lineas_pedido4:   #Confimarcion que el pedido sea valido
        #     print(lineas_pedido4.producto, " pidio ", lineas_pedido4.cantidad)
        
        enviar_mail(
            pedido = pedido,
            lineas_pedido = lineas_pedido4,
            nombreusuario = request.user.username,
            emailusuario = request.user.email
        )

        #messages.success(request, "El pedido se realizado satisfactoriamente")

        return redirect("/autenticacion/perfil")
    else: 
        # pass
        info_usuario = usuarios.objects.all()
        return render(request, "stock/checkout.html", {"info_usuario":info_usuario, "pedido_valido": pedido_valido})
        # return render(request, "stock/carrito.html", {"pedido_valido": pedido_valido})
        # return render(request, "stock/home.html", {"arts":arts, "articulos":ultimos_articulos})

def enviar_mail(pedido, lineas_pedido, nombreusuario, emailusuario, **kwargs):

    asunto="Comprobante de pedido"
    mensaje = render_to_string("emails/pedido.html",{

        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "nombreusuario": nombreusuario

    })


    mensaje_texto=strip_tags(mensaje)
    from_email="kaorigtshop2@gmail.com"         ########Correo desde el que se envia        aajekdjonxyejtih 
    to=emailusuario               ########Correo desde al que se envia
    # to = "francoabimael07@gmail.com"

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)


# def enviar_mail(**kwargs):

#     asunto="Comprobante de pedido"
#     mensaje = render_to_string("emails/pedido.html",{

#         "pedido": kwargs.get("pedido"),
#         "lineas_pedido": kwargs.get("lineas_pedido"),
#         "nombreusuario": kwargs.get("nombreusuario")

#     })


#     mensaje_texto=strip_tags(mensaje)
#     from_email="kaorigtshop@gmail.com"         ########Correo desde el que se envia        aajekdjonxyejtih 
#     to=kwargs.get("emailusuario")               ########Correo desde al que se envia
#     # to = "francoabimael07@gmail.com"

#     send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)