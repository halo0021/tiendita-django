
from django.shortcuts import get_object_or_404, redirect, render
from productos.models import Producto
from .models import Carro, CarroItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _carro_id(request):
    carro=request.session.session_key
    if not carro:
        carro= request.session.create()
    return carro  

#crear carrito
def agregar_carro(request, producto_id):
    producto= Producto.objects.get(id=producto_id)

    try:
        carro=Carro.objects.get(carro_id=_carro_id(request))
    except Carro.DoesNotExist:
        carro=Carro.objects.create(
            carro_id=_carro_id(request)
        )
    carro.save()
    try:
        carro_item=CarroItem.objects.get(producto=producto, cart=carro)
        carro_item.cantidad +=1
        carro_item.save()
    except CarroItem.DoesNotExist:
        carro_item=CarroItem.objects.create(
            producto=producto,
            cantidad=1,
            cart=carro,

        )
        carro_item.save()
    return redirect('cart')

def eliminar_carro(request,producto_id):
    cart=Carro.objects.get(carro_id=_carro_id(request))
    producto= get_object_or_404(Producto, id=producto_id)
    cart_item = CarroItem.objects.get(producto=producto,cart=cart)
    
    if cart_item.cantidad>1:
        cart_item.cantidad -=1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def eliminar_carro_item(request, producto_id):
 cart=Carro.objects.get(carro_id=_carro_id(request))
 producto= get_object_or_404(Producto, id=producto_id)
 cart_item = CarroItem.objects.get(producto=producto,cart=cart)
 cart_item.delete()
 return redirect('cart')
def carro(request, total=0, cantidad=0, carro_item=None):
    try:
        carro= Carro.objects.get(carro_id=_carro_id(request))
        carro_items =CarroItem.objects.filter(cart=carro, activado=True)
        for carro_item in carro_items:
            total += (carro_item.producto.precio * carro_item.cantidad)
            cantidad += carro_item.cantidad
        inpuesto=(12*total)/100
        grand_total= total * inpuesto
    except ObjectDoesNotExist:
        pass
    context={
        'total':total,
        'cantidad':cantidad,
        'carro_items':carro_items,
        'inpuesto':inpuesto,
        'grand_total':grand_total,


    }

    return render(request,'productos/carro.html',context)