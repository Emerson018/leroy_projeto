from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from produtos.models import Produto


def index(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/index.html',{"cards": produtos})

def imagem(request):
    return render(request, 'produtos/imagem.html')

