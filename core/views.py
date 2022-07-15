from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import *
from urllib import request
from django.shortcuts import render

# Create your views here.
def root(request):
    return redirect('home')

def home(request):
    return render(request,'core/home.html',)

def quienessomos(request):
    return render(request,'core/quienessomos.html',)

def donaciones(request):
    return render(request,'core/donaciones.html',)

def herramientas(request):
    ProductosHerramientas = Producto.objects.filter(tipo_id=1)
    return render(request,'core/herramientas.html', {"productos":ProductosHerramientas})

def plantas(request):
    ProductosPlantas = Producto.objects.filter(tipo_id=2)
    return render(request,'core/plantas.html', {"productos":ProductosPlantas})


def carrito(request):
    return render(request,'core/carrito.html',)

def despacho_vendedor(request):
    return render(request,'core/despacho_vendedor.html',)

def login(request):
    return render(request,'core/login.html',)

def pago(request):
    return render(request,'core/pago.html',)

def productoh1(request):
    return render(request,'core/producto h1.html',)

def productoh2(request):
    return render(request,'core/producto h2.html',)

def productoh3(request):
    return render(request,'core/producto h3.html',)

def productoh4(request):
    return render(request,'core/producto h4.html',)

def productop1(request):
    return render(request,'core/producto p1.html',)

def productop2(request):
    return render(request,'core/producto p2.html',)

def productop3(request):
    return render(request,'core/producto p3.html',)

def productop4(request):
    return render(request,'core/producto p4.html',)

    

#def product_by_ZA(request):
#    productos = ordering=['-marca']
#   return render(request,'core/herramientas.html',{'productos':productos})

#def test(request):
#  contexto = {"nombre":"Mundo"}
#   return render(request, '', contexto)
#
