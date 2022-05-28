import imp
from django.contrib import admin
from .models import Carro,CarroItem
# Register your models here.

admin.site.register(Carro)
admin.site.register(CarroItem)