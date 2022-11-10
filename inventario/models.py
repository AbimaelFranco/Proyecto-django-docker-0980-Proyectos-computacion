from tabnanny import verbose
from django.db import models

class articulos(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    categoria = models.CharField(max_length=30, null=False)
    precio = models.FloatField(null=False)
    descuento = models.FloatField(null=False)
    descripcion = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='servicios')
    cantidad = models.IntegerField(null=False, default= 0)
    disponibilidad = models.BooleanField()
    creacion = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'articulo'

    def __str__(self):
        return self.nombre

# class clientes(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     dpi = models.IntegerField()
#     telefono = models.IntegerField()
#     direccion = models.CharField(max_length=150)