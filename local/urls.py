from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("terminos/", views.terminos, name="terminos"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil_log/", views.perfil_log, name="perfil-log"),
    path("productos/", views.productos, name="productos"),
    path("registro/", views.registro, name="registro"),
    path("inicio_sesion/", views.inicio_sesion, name="inicio_sesion"),
    path("logout/", views.cerrar_sesion, name="cerrar_sesion"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name="Add"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="Del"),
    path("restar/<int:producto_id>/", views.restar_producto, name="Sub"),
    path("limpiar/", views.limpiar_producto, name="CLS"),
]
