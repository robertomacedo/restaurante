from django.urls import path 
from . import views


urlpatterns = [
    path('mesa/<slug:slug>/', views.mesa_cliente, name='mesa_cliente'),
    path('cardapio/<slug:slug>/', views.cardapio_cliente, name='cardapio_cliente'),
]