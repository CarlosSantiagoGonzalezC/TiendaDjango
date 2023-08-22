from django.db import models

# Create your models here.
class Categoria(models.Model):
    catNombre = models.CharField(max_length=50, unique=True)
    catFoto = models.FileField(upload_to='fotos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.catNombre

class Producto(models.Model):
    proCodigo = models.IntegerField(unique=True)
    proNombre = models.CharField(max_length=50)
    proPrecio = models.IntegerField()
    proCategoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proFoto = models.FileField(upload_to='fotos/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.proNombre