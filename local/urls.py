from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("terminos/", views.terminos, name="terminos"),
    path("perfil/", views.perfil, name="perfil"),
    path("registro/", views.registro, name="registro"),
    path("inicio_sesion/", views.sesion, name="inicio_sesion"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion"),
]
