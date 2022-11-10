from email.policy import default
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from inventario.models import articulos
from django.db.models import F, Sum, FloatField

User = get_user_model()

class Pedido(models.Model):

#############################################################################
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    entregado = models.BooleanField(default=False)
    operacion = models.CharField(max_length=50, null=False, default='compra')
    created_at = models.DateTimeField(auto_now_add=True)
#############################################################################

    def __str__(self):
        return self.operacion

    @property
    def total(self):
        return self.lineapedido_set.agregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name='pedido'
        verbose_name_plural = 'pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(articulos, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    operacion = models.CharField(max_length=50, null=False, default='compra')
    cantidad = models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    def __str__(self):
        return self.operacion

    class Meta:
        db_table = 'lineapedidos'
        verbose_name='Linea pedido'
        verbose_name_plural = 'Lineas pedidos'
        ordering=['id']