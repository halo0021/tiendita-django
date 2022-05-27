from audioop import reverse
from django.db import models
from django.urls import reverse
 
# Create your models here.
class Categoria(models.Model):
  nombre_categoria= models.CharField(max_length=20, unique=True)
  descripcion = models.CharField(max_length=255, blank= True)
  slug = models.CharField(max_length=100, unique=True)
  cat_img = models.ImageField(upload_to='photos/categorias', blank=True)
 
  class Meta:
      verbose_name='categoria'
      verbose_name_plural='categorias'
# sacamos el slug de url de la app de productos
# pasamos por el self el objeto categoria y le pedimos o camputramos el slug
  def get_url(self):
      return reverse('productos_de_categoria',args=[self.slug])
      #http://localhost:8000/productos/´armas´  <- esto dispara la funcion y se consulta en la base de datos
      #en si consulta si esta esa categoria armas  y lo manda  para que se muestre en la lista
  def __str__(self):
      return self.nombre_categoria
      