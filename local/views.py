from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout

# Create your views here.
def home(request):
    return render(request, "local/index.html")

def nosotros(request):
    return render(request, "local/nosotros.html")

def terminos(request):
    return render(request, "local/terminos.html")

def perfil(request):
    return render(request, "local/profile.html")

def registro(request):
    if request.method == 'GET':
        return render(request, "local/registro.html",{
            'form' : UserCreationForm
    })  
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    
                )
            except:
                return render(request, "local/registro.html",{
            'form' : UserCreationForm,
            'error' : 'El usuario ya existe'
            })  
        return render(request, "local/registro.html",{
            'form' : UserCreationForm,
            'error' : 'Las contraseñas no coinciden'
    })  

def sesion(request):
    return render(request, "local/inicio_sesion.html")

def cerrar_sesion(request):
    logout(request)
    return redirect('index')