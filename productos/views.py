
from django.shortcuts import get_object_or_404, render
from carrito.models import CarroItem
from .models import Producto
from categoria.models import Categoria
from carrito.models import CarroItem
from carrito.views import _carro_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q 
# Create your views here.

def productos(request, categoria_slug=None):
    categorias = None
    productos= None

    if categoria_slug != None :
        categorias = get_object_or_404(Categoria, slug=categoria_slug)# si en cuentra la categoria   le enlista  y si no la encuentra mandara  un error 404
        productos = Producto.objects.filter(categoria=categorias,valido=True).order_by('id')
        paginator =Paginator(productos,10)
        page= request.GET.get('page')
        paged_productos=paginator.get_page(page)
        producto_cantidad= productos.count()
    else:
      productos=  Producto.objects.all().filter(valido=True).order_by('id')
      #aqui indicamos cuantos elementos queremos adentor de  la pagina
      paginator =Paginator(productos,10)
      page= request.GET.get('page')
      paged_productos=paginator.get_page(page)
      #-------
      producto_cantidad= productos.count()
    
    
    context={
        'productos':paged_productos,
        'producto_cantidad':producto_cantidad,
    }
    return render(request, 'productos/productos.html',context)

def productos_detalle(request,categoria_slug,producto_slug):

#se busca por el slug la categoria  y el producto por el slug
    try:
        single_producto = Producto.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
        in_cart =CarroItem.objects.filter(cart__carro_id=_carro_id(request), producto=single_producto).exists()
    except Exception as e:
           raise e
    #si se encuentra el producto en la base de datos se  guarda en un dicionario y lo mandamos
    #por el render
    context={
        'single_producto': single_producto,
        'in_cart':in_cart,
    }

    return render(request,'productos/producto_detalles.html', context)


def buscar(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
    if keyword:
        productos= Producto.objects.order_by('-fecha_creacion').filter(Q(descripcion__icontains=keyword) | Q(nombre_producto=keyword)) 
        productos_count=productos.count()
        context={
            'productos':productos,
            'productos_count':productos_count,
        } 
    return render(request,'productos/productos.html',context)