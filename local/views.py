from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import CustomUserForm
from django.contrib.auth.models import User
from .models import Product
from local.carrito import Carrito

# Create your views here.
def home(request):
    return render(request, "local/index.html")

def nosotros(request):
    return render(request, "local/nosotros.html")

def terminos(request):
    return render(request, "local/terminos.html")

def perfil_log(request):
    return render(request, "local/profile_log.html")

def perfil(request):
    return render(request, "local/profile.html")

def productos(request):
    productos = Product.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, "local/productos.html",data)

def registro(request):
    if request.method == 'GET':
        return render(request, 'local/registro.html',{
            'form' : CustomUserForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except: 
                return render(request, 'local/registro.html',{
                    'form' : CustomUserForm,
                    "error" : 'El nombre de usuario ya existe'
                })
        return render(request, 'local/registro.html',{
                    'form' : CustomUserForm,
                    "error" : 'Las contraseñas no coinciden'
                })
        
    return render(request, "local/registro.html")  

def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, "local/inicio_sesion.html",{
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(
            request,username=request.POST['username'], 
            password=request.POST['password'])
        if user is None:
            return render(request, 'inicio_sesion',{
                'form' : AuthenticationForm,
                'error' : 'Usuario o contraseña incorrecta'
            })
        else:
            login(request,user)
            return redirect(to='home')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Product.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("productos")

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("productos")