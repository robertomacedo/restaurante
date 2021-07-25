from django.urls import path
from .views import *


app_name = 'usuario'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('entrar/', LoginView.as_view(), name='entrar'),
]