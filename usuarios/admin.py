from django.contrib import admin
from .models import usuarios
# Register your models here.

# @admin.register(usuarios)
# class UsuariosAdmin(admin.ModelAdmin):
#     list_display=['cui', 'username']
#     list_display_links=['username']



    # readonly_fields=('login_attempts', 'active_account')

# admin.site.register(Usuarios, UsuariosAdmin)


class UsuariosAdmin(admin.ModelAdmin):
    fields=('user','fisrt_name', 'last_name', 'username', 'cui', 'email', 'login_attempts')
    readonly_fields=('user','fisrt_name', 'last_name', 'username', 'cui', 'email', 'login_attempts') #Evitar la modificacion en la edicion de registro
    list_display = ['last_name', 'fisrt_name', 'username', 'email', 'cui'] #Propiedades visibles del campo
    ordering = ['last_name']    #Ordena registros por
    search_fields = ['last_name', 'username', 'cui'] #Permite buscar por
    # list_display_links = [''] #brindar link a campo
    # list_filter=['']  #Añadir buscar por filtro
    list_per_page=15    #Cantidad de items por pagina
    # exclude=['']      #Excluir campos en la edicion de registro

admin.site.register(usuarios, UsuariosAdmin)

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