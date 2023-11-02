from django.shortcuts import render, redirect
from django.contrib import messages
from produtos.models import Produto
from produtos.conteudo.search_data import data_get, find_price
from produtos.conteudo.format_values import format_real, format_cents
from .forms import ProdutoForm
from bs4 import BeautifulSoup
import requests

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

def lista(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['link']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
                
            try:    
                req = requests.get(url,headers=headers)
                req.raise_for_status()
                html_content = req.text
                soup = BeautifulSoup(html_content,"html.parser")

                title   = soup.find('h1', class_='product-title align-left color-text').text.replace('\n', '')

                barcode = soup.find('div', class_='badge product-code badge-product-code').text
                lm = ''
                for caractere in barcode:
                    if caractere.isdigit():
                        lm += caractere

                prod_price = soup.find('div',class_='product-price-tag')

                price = find_price(prod_price)
                reais = format_real(price)
                centavos = format_cents(price)
                preco = (reais + centavos)

                

                return render(request, 'produtos/lista.html', {'title': title, 'lm': lm, 'preco':preco})
            
            except requests.exceptions.RequestException as e:
                messages.error(request, 'Erro ao acessar a página do produto')
        
        else:
            messages.error(request, 'Formulário inválido. Certifique-se de inserir o link correto.')
    
    else:
        form = ProdutoForm()

    return render(request, 'produtos/lista.html', {'form':form})

#passar a variável 'soup' pra dentro 
