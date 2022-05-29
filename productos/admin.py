from django.contrib import admin
from .models import Producto,Variacion
# Register your models here.

#muestra los detalles de los productos al administrador
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio','stock','categoria','fecha_modificacion','valido')
    prepopulated_fields = {'slug':('nombre_producto',)}
#
class VariacionAdmin(admin.ModelAdmin):
    list_display=('producto', 'variacion_categoria', 'variacion_value', 'valido')
    list_editable=('valido',)
    list_filter = ('producto', 'variacion_categoria', 'variacion_value', 'valido')
    



admin.site.register(Producto, ProductAdmin)
admin.site.register(Variacion,VariacionAdmin)
