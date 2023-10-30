from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from produtos.models import Produto


def index(request):
    produto = Produto.objects.order_by("-data_produto")
    return render(request, 'produtos/index.html',{"cards": produto})

def imagem(request):
    return render(request, 'produtos/imagem.html')

def buscar(request):
    produtos = Produto.objects.order_by("-data_produto")

    if "buscar"  in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            produtos = produtos.filter(titulo__icontains=nome_a_buscar)

    return render(request, 'produtos/buscar.html', {"cards": produtos})