from django.urls import path
from . import views

urlpatterns =[
    path('', views.productos, name="productos"),
    path('categoria/<slug:categoria_slug>/',views.productos,name='productos_de_categoria'),# path dinamico
    path('categoria/<slug:categoria_slug>/<slug:producto_slug>/',views.productos_detalle, name='productos_detalle'),
    path('buscar/', views.buscar, name='buscar'),
]