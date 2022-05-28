from django.urls import path
from . import views

urlpatterns = [
    path('', views.carro, name='cart'),
    path('agregar_carro/<int:producto_id>/', views.agregar_carro, name='agregar_carro'),
    path('eliminar_carro/<int:producto_id>/', views.eliminar_carro, name='eliminar_carro'),
    path('eliminar_carro_item/<int:producto_id>/', views.eliminar_carro_item, name='eliminar_carro_item'),
]