from django.contrib import admin
from .models import *


admin.site.register([Mesa, Comanda, Categoria, ItemCardapio, ItemPedido])
