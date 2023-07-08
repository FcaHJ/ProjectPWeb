from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "local/index.html")

def nosotros(request):
    return render(request, "local/nosotros.html")

def terminos(request):
    return render(request, "local/terminos.html")

def perfil(request):
    return render(request, "local/profile.html")