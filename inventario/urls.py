from xml.dom.minidom import Document
from django.urls import path
from inventario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.catalogo, name="Catalogo"),
    path('producto/<int:id>', views.single_product, name="Producto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)