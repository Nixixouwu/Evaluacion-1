from distutils.command.upload import upload
from hashlib import blake2b
from tabnanny import verbose
from django.db import models

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='ID')
    marca = models.CharField(max_length=50, verbose_name='Marca')

    class Meta:
        verbose_name='marca'
        verbose_name_plural='marcas'
        ordering=['marca']

    def __str__(self):
        return self.marca

class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='ID')
    tipo = models.CharField(max_length=50, verbose_name='Tipo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='tipo'
        verbose_name_plural='tipos'
        ordering=['tipo']

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE,null=True,blank=True)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE,null=True,blank=True)
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos',null=True,blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        ordering=['idProducto']

    def __str__(self):
        return self.descripcion


# Create your models here.
