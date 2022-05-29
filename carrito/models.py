from django.db import models
from productos.models import Producto,Variacion


# Create your models here.

class Carro(models.Model):
      carro_id=models.CharField(max_length=250,blank=True)
      fecha_agregacion= models.DateField(auto_now_add=True)

      def __str__(self):
            return self.carro_id

class CarroItem(models.Model):

    producto= models.ForeignKey(Producto,on_delete=models.CASCADE)
    variaciones=models.ManyToManyField(Variacion, blank=True)
    cart= models.ForeignKey(Carro,on_delete=models.CASCADE)
    cantidad= models.IntegerField()
    activado= models.BooleanField(default=True)
    def sub_total(self):
          return self.producto.precio * self.cantidad
    def __unicode__(self) :
         return self.producto

