from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


class HomeView(TemplateView):
    template_name = 'usuario/home.html'


class LoginView(LoginView):
    template_name = 'entrar.html'