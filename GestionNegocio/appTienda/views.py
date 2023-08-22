from django.shortcuts import redirect, render
from appTienda.models import Producto, Categoria
from django.db import Error
from GestionNegocio.settings import MEDIA_ROOT
from os import remove

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


def vistaAgregarProducto(request):
    categorias = Categoria.objects.all()
    retorno = {"listaCategorias":categorias}
    return render(request, "frmAgregarProducto.html", retorno)


def vistaAgregarCategoria(request):
    return render(request, "frmAgregarCategoria.html")


def agregarProducto(request):
    codigo = int(request.POST["txtCodigo"])
    nombre = request.POST["txtNombre"]
    precio = int(request.POST["txtPrecio"])
    idCategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES["fileFoto"]
    
    try:
        categoria = Categoria.objects.get(id=idCategoria)
        producto = Producto(proCodigo=codigo, proNombre=nombre, 
                            proPrecio=precio, proFoto = archivo, proCategoria=categoria)
        producto.save()
        mensaje = "Producto agregado correctamente..."
        return redirect("/listarProductos/")
        
    except Error as error:
        mensaje = f"Problemas a la hora de agregar el producto. {error}"
    
    retorno = {"mensaje":mensaje, "producto":producto}
    
    return render(request, "frmAgregarProducto.html", retorno)


def listarProductos(request):
    try:
        productos = Producto.objects.all()
        mensaje = ""
        print(productos)
        
    except:
        mensaje = "Problemas al obtener los productos!!"
    
    retorno = {"mensaje":mensaje, "listaProductos":productos}
    
    return render(request, "listarProductos.html", retorno)


def listarCategorias(request):
    try:
        categorias = Categoria.objects.all()
        mensaje = ""
        print(categorias)
        
    except:
        mensaje = "Problemas al obtener las categorias!!"
    
    retorno = {"mensaje":mensaje, "listaCategorias":categorias}
    
    return render(request, "listarCategorias.html", retorno)


def agregarCategoria(request):
    nombre = request.POST["txtNombre"]
    
    try:
        categoria = Categoria(catNombre=nombre)
        categoria.save()
        mensaje = "Categoria agregada correctamente..."
        return redirect("/listarCategorias/")
        
    except Error as error:
        mensaje = f"Problemas a la hora de agregar la categoria. {error}"
    
    retorno = {"mensaje":mensaje, "categoria":categoria}
    
    return render(request, "frmAgregarCategoria.html", retorno)


def consultarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        categorias = Categoria.objects.all()
        mensaje = ""
        
    except Error as error:
        mensaje = f"Problemas. {error}"
    
    retorno = {"mensaje":mensaje, "producto":producto, "listaCategorias":categorias}
    
    return render(request, "frmEditarProducto.html", retorno)


def actualizarProducto(request):
    idProducto = int(request.POST["idProducto"])
    codigo = int(request.POST["txtCodigo"])
    nombre = request.POST["txtNombre"]
    precio = int(request.POST["txtPrecio"])
    idCategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES.get("fileFoto", False)
    
    try:
        categoria = Categoria.objects.get(id=idCategoria)
        producto = Producto.objects.get(id=idProducto)
        producto.proCodigo=codigo
        producto.proNombre=nombre
        producto.proPrecio=precio
        producto.proCategoria=categoria
        
        if archivo != '':
            producto.proFoto = archivo
        
        producto.save()
        mensaje = "Producto actualizado correctamente..."
        return redirect("/listarProductos/")
        
    except Error as error:
        mensaje = f"Problemas a la hora de actualizar el producto. {error}"
    
    categorias = Categoria.objects.all()
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "producto":producto}
    
    return render(request, "frmEditarProducto.html", retorno)


def eliminarProducto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        path = f"{MEDIA_ROOT}/{producto.proFoto}"
        remove(path)
        producto.delete()
        mensaje = "Producto eliminado correctamente..."
        
    except Error as error:
        mensaje = f"Problemas a la hora de eliminar el producto. {error}"
    
    retorno = {"mensaje":mensaje}
    
    return redirect("/listarProductos/", retorno)


from rest_framework import generics
from appTienda.models import Categoria, Producto
from appTienda.serializers import CategoriaSerializer, ProductoSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer