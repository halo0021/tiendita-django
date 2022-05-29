
from django.urls import reverse
from django.db import models
from categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    nombre_producto= models.CharField(max_length=200,unique=True)
    slug = models.CharField(max_length=200,unique=True)
    descripcion=models.CharField(max_length=500,blank=True)
    precio= models.IntegerField()
    imagen= models.ImageField(upload_to='photos/productos')
    stock=models.IntegerField()
    valido=models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # se invoca  como si clave  foranea y si se borra  la categoria  se borra los productos relacionados 
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_modificacion=models.DateField(auto_now=True)

    def get_url(self):
        #  se llama  el get url  desde  lo ulrs esto quiere decir que nesesitamos 2 parametros  como se ven en el 
        #path de ulrsse nesesita el slug de categoria  y producto
        return reverse('productos_detalle', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return  self.nombre_producto


# para filtar  el color y talla
class VariacionManager(models.Manager):
      
      def colors(self):
          return super(VariacionManager, self).filter(variacion_categoria='color', valido=True)
       
      def tallas(self):
          return super(VariacionManager, self).filter(variacion_categoria='talla', valido=True)

variacion_categoria_choice=(
  ('color','color'),
  ('talla','talla'),

)

# sirve  para hacer variaciones  como color  o talla
class Variacion(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    variacion_categoria= models.CharField(max_length=100, choices=variacion_categoria_choice)
    variacion_value= models.CharField(max_length=100)
    valido=models.BooleanField(default=True)
    fecha_creacion= models.DateTimeField(auto_now=True)
    
    objects= VariacionManager()

    def __str__(self) :
        return self.variacion_categoria + ':' + self.variacion_value

