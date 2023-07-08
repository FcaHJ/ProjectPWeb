from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("terminos/", views.terminos, name="terminos"),
    path("perfil/", views.perfil, name="perfil"),
]
