from xml.dom.minidom import Document
from django.urls import path
from stock import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('carrito', views.carrito, name="Carrito"),
    path('contacto', views.contacto, name="Contacto"),
    path('checkout', views.checkout, name="Checkout"),
    path('manual_usuario', views.manual_usuario, name="manual_usuario"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)