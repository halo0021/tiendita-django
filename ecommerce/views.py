from django.shortcuts import render
from productos.models import Producto
def home(request):
    productos = Producto.objects.all().filter(valido=True)#<- pedimos los productos que estan activos
    context ={
        'productos':productos
    }
    return render(request,'home.html',context)
