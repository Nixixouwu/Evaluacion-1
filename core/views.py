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
    return render(request,'core/herramientas.html',)

def plantas(request):
    return render(request,'core/plantas.html',)

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

    
#def test(request):
#  contexto = {"nombre":"Mundo"}
#   return render(request, '', contexto)
#
