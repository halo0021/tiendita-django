


from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Producto
from categoria.models import Categoria
# Create your views here.

def productos(request, categoria_slug=None):
    categorias = None
    productos= None

    if categoria_slug != None :
        categorias = get_object_or_404(Categoria, slug=categoria_slug)# si en cuentra la categoria   le enlista  y si no la encuentra mandara  un error 404
        productos = Producto.objects.filter(categoria=categorias,valido=True)
        producto_cantidad= productos.count()
    else:
      productos=  Producto.objects.all().filter(valido=True)
      producto_cantidad= productos.count()
    
    
    context={
        'productos':productos,
        'producto_cantidad':producto_cantidad,
    }
    return render(request, 'productos/productos.html',context)

def productos_detalle(request,categoria_slug,producto_slug):

#se busca por el slug la categoria  y el producto por el slug
    try:
        single_producto = Producto.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
    except Exception as e:
           raise e
    #si se encuentra el producto en la base de datos se  guarda en un dicionario y lo mandamos
    #por el render
    context={
        'single_producto': single_producto,
    }

    return render(request,'productos/producto_detalles.html', context)

