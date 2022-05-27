from django.urls import path
from . import views

urlpatterns =[
    path('', views.productos, name="productos"),
    path('<slug:categoria_slug>/',views.productos,name='productos_de_categoria'),# path dinamico
    path('<slug:categoria_slug>/<slug:producto_slug>/',views.productos_detalle, name='productos_detalle'),
]