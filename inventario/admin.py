from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import articulos


class serviciosresource(resources.ModelResource):
    fields =('id', 'nombre', 'categoria', 'precio', 'descripcion', 'creacion', 'cantidad')
    
    class Meta:
        model = articulos


@admin.register(articulos)
class ServiciosAdmin(ImportExportModelAdmin):
    resource_class = serviciosresource
    readonly_fields=('creacion', 'update')
    list_display = ['nombre', 'disponibilidad', 'categoria', 'precio', 'descuento'] #Propiedades visibles del campo
    list_filter=['categoria', 'disponibilidad']  #Añadir buscar por filtro
    list_per_page=15    #Cantidad de items por pagina
    list_editable=['disponibilidad',]

# admin.site.register(articulos, ServiciosAdmin)


"""
    list_display = ['last_name', 'fisrt_name', 'username', 'email', 'cui'] #Propiedades visibles del campo
    ordering = ['last_name']    #Ordena registros por
    search_fields = ['last_name', 'username', 'cui'] #Permite buscar por
    # list_display_links = [''] #brindar link a campo
    # list_filter=['']  #Añadir buscar por filtro
    list_per_page=15    #Cantidad de items por pagina
    readonly_fields=('cui', 'username') #Evitar la modificacion en la edicion de registro
    # exclude=['']      #Excluir campos en la edicion de registro
"""