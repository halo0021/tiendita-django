from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  Cuenta

class AccountAdmin(UserAdmin):

    list_display =('email','nombre','apellido','username','fecha_registro','ultima_conexion','is_active')#<-- se mostratran las propiedades del usuario
    list_display_link=('email','nombre','apellido') # <-- si se me hace  click a las columnas mostrara esos datos
    readonly_fields=('fecha_registro','ultima_conexion') #<-- mostrara  la ultima vez que ingreos el usuario
    ordering=('-ultima_conexion',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()

# Register your models here.
admin.site.register(Cuenta,AccountAdmin)