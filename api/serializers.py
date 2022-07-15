from rest_framework import serializers
from crud.models import Producto, Marca, Tipo

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto','descripcion','precio','stock','marca','tipo','created_at','updated_at')

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id','marca')

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ('id','tipo','created_at','updated_at')
