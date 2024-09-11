from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# ANOTAÇÕES - Guilherme
# Arquivo responsável por definir as regras de negócio do app. Vulgo ACTION.
# E onde está o html para ser exibido depois.

# Create your views here.

from django.shortcuts import render

def home(request):
    return redirect('auth/login')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'auth/cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se nome de usuario ja esta em uso
        if User.objects.filter(username=nome).exists():
            return HttpResponse('Nome de usuario já existente')

        # Salva usuario
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return HttpResponse('Usuario cadastrado com sucesso!')
        return HttpResponse(nome)


def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(email=email, password=senha)
        if user:
            login_django(request,user)
            return HttpResponse('autentificado')
        else:
            return HttpResponse('email ou senha invalidos')


@login_required(login_url='/auth/login/')
def plataforma(request):
    return HttpResponse('plataforma')