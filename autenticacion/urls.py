from django.urls import path
from . import views 
from .views import cerrar_sesion,logear


urlpatterns = [
     path('', views.main, name='main'),
     path("cerrar_sesion",cerrar_sesion,name="cerrar_sesion"),
     path("logear",logear,name="logear"),
     path("registro/", views.registro_usuario, name='registro'),
]