from rest_framework import serializers
from appTienda.models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'catNombre', 'catFoto', 'created_at', 'updated_at')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'proCodigo', 'proNombre', 'proPrecio', 'proCategoria', 'proFoto', 'created_at', 'updated_at')
