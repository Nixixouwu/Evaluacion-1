from django.shortcuts import render,redirect,reverse
from .models import *
from .forms import *

# Create your views here.

def product_list(request):
    context = {'productos':Producto.objects.all()}
    return render(request,'crud/product_list.html',context)

def product_delete(request,product_id):
    try:
        producto = Producto.objects.get(idProducto=product_id)
        producto.delete()
        return redirect(reverse('product-list') + "?DELETED")
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