from . models import Carro, CarroItem
from .views import _carro_id

def counter(request):
    cart_count=0
    try:
        cart=Carro.objects.filter(carro_id=_carro_id(request))
        cart_items=CarroItem.objects.all().filter(cart=cart[:1])
        #saber la cantidad de productos

        for cart_item in cart_items:
            cart_count +=cart_item.cantidad
    except Carro.DoesNotExist:
        cart_count=0
    return dict(cart_count=cart_count)