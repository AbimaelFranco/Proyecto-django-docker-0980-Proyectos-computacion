from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import Pedido, LineaPedido



class pedidosresource(resources.ModelResource):
    fields =('id', 'operacion', 'user_id', 'created_at')
    
    class Meta:
        model = Pedido


# @admin.register(Pedido)
class PedidosAdmin(ImportExportModelAdmin):
    resource_class = pedidosresource
    readonly_fields=('id', 'user','created_at','operacion')
    fields=('id','user','created_at','operacion','entregado',)
    list_display = ('id', 'user', 'created_at','entregado' ) #Propiedades visibles del campo
    list_display_links = ['id',] #brindar link a campo
    list_filter=['created_at']  #Añadir buscar por filtro
    search_fields = ['id', 'user'] #Permite buscar por
    list_editable=['entregado',]
    # list_per_page=15    #Cantidad de items por pagina
    # list_editable=['disponibilidad',]

class LineapedidosAdmin(admin.ModelAdmin):
    readonly_fields=('id','user','created_at')
    fields=('id','user','created_at')
    list_display = ('id', 'user', 'created_at', ) #Propiedades visibles del campo
    list_display_links = ['id',] #brindar link a campo
    list_filter=['created_at']  #Añadir buscar por filtro
    search_fields = ['id', 'user'] #Permite buscar por
    # list_editable=['entregado',]
    # list_per_page=15    #Cantidad de items por pagina
    # list_editable=['disponibilidad',]

# admin.site.register([Pedido, LineaPedido], PedidosAdmin)
admin.site.register(Pedido, PedidosAdmin)