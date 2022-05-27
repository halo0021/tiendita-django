from .models import Categoria

# aqui hacemos publico  los menu links en TEMPLATE  en settings en   ecomecenter
def menu_links(request):
    links = Categoria.objects.all() # vienen las categorias de la base de datos  o en si se hace una consulta
    return dict(links=links) #retorna en un dicionario   en  con los links

