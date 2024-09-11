from django.shortcuts import render

# ANOTAÇÕES - Guilherme
# Arquivo responsável por definir as regras de negócio do app.
# E onde está o html para ser exibido depois.

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')