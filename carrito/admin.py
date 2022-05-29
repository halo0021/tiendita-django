
from django.contrib import admin
from .models import Carro,CarroItem
# Register your models here.
class CarroAdmin(admin.ModelAdmin):
      list_display=('carro_id','fecha_agregacion')

class CarroItemAdmin(admin.ModelAdmin):
    list_display=('producto','cart','cantidad','activado')


admin.site.register(Carro,CarroAdmin)
admin.site.register(CarroItem,CarroItemAdmin)