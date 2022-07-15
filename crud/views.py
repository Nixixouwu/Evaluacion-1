from django.shortcuts import render,redirect,reverse
from .models import *
from .forms import *
# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/product_list.html',context)

def product_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            idProducto = form.cleaned_data.get("idProducto")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            marca = form.cleaned_data.get("marca")
            tipo = form.cleaned_data.get("tipo")
            imagen = form.cleaned_data.get("imagen")
            obj = Producto.objects.create(
                idProducto=idProducto,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                marca=marca,
                tipo=tipo,
                imagen=imagen
            )
            obj.save()
            return redirect(reverse('product-list')+"?OK")
        else:
            return redirect(reverse('product-list')+"?FAIL")
    else:
        form = ProductoForm
    return render(request,'crud/product_new.html',{'form':form})

def product_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(reverse('product-list') + "?DELETED")
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_detail(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            context = {'producto':producto}
            return render(request,'crud/product_detail.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_edit(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        if producto:
            form = ProductoForm(instance=producto)
        else:
            return redirect(reverse('product-list') + "?FAIL")

        if request.method == 'POST':
            form = ProductoForm(request.POST,request.FILES,instance=producto)
            if form.is_valid():
                form.save()
                return redirect(reverse('product-list') + "?SUCCESS")
            else:
                return redirect(reverse('product-edit') + product_id)
        context = {'form':form}
        return render(request,'crud/product_edit.html',context)
    except:
        return redirect(reverse('product-list') + "?FAIL")

def product_by_marca(request,marca):
    productos = Producto.objects.filter(marca=marca)
    return render(request,'crud/product_list.html',{'productos':productos})

def product_by_tipo(request,tipo):
    productos = Producto.objects.filter(tipo=tipo)
    return render(request,'crud/product_list.html',{'productos':productos})
