from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from produtos.models import Produto
from produtos.conteudo.search_data import *
from produtos.conteudo.format_values import format_real, format_cents
from .forms import ProdutoForm
from urllib.parse import unquote

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a página.')
        return redirect('login')
    
    produto = Produto.objects.order_by("-data_produto")
    return render(request, 'produtos/index.html',{"cards": produto})

def imagem(request):
    return render(request, 'produtos/imagem.html')

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para pesquisar.')
        return redirect('login')
    
    produtos = Produto.objects.order_by("-data_produto")

    if "buscar"  in request.GET:
        termo_busca = request.GET['buscar']
        if termo_busca:
            produtos = produtos.filter(Q(titulo__icontains=termo_busca) | Q(lm__icontains=termo_busca))
            
    return render(request, 'produtos/buscar.html', {"cards": produtos})

def lista(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['link']
            
            if 'leroymerlin.com.br' not in url:
                messages.error(request, 'Formulário inválido. Certifique-se de inserir o link correto.')
                return redirect('lista')

            html_content = requisition(url).find('h1', class_='product-title align-left color-text')
                
            if html_content:
                title, lm = get_title_and_lm(url, html_content)
                html_price = requisition(url).find('div',class_='product-price-tag')
                price = find_price(html_price)
                reais = format_real(price)
                centavos = format_cents(price) 
                preco = (reais + centavos)
                review, average_review = get_review(lm)
                foto = get_image(url)

                if lm:
                    if Produto.objects.filter(lm=lm).exists():
                        messages.error(request, 'Produto já existente.')

                        return redirect('lista')
                    else:
                        produto = Produto(
                            lm=lm,
                            titulo=title,
                            preco=preco,
                            link=url,
                            avaliacoes=review,
                            media_avaliacoes=average_review,
                            foto=foto)
                        
                        produto.save()
                        messages.success(request, 'Produto salvo com sucesso!')

                        return render(
                            request,
                            'produtos/lista.html',
                            {'title': title,
                             'lm': lm,
                             'preco':preco,
                             'url': url,
                             'avaliacoes': review,
                             'media_avaliacoes': average_review,
                             'foto': foto
                            }
                        )
            
            else:
                messages.error(request, 'Certifique-se de inserir o link de um PRODUTO.')
                return render(request, 'produtos/lista.html')
    
    else:
        form = ProdutoForm()

    return render(request, 'produtos/lista.html', {'form':form})

def dados(request):
    dados = Produto.objects.all()

    return render(request, 'produtos/dados.html', {'dados': dados})

def detalhe_produto(request):
    lm = request.GET.get('lm')
    titulo = unquote(request.GET.get('titulo'))
    produto = Produto.objects.get(lm=lm, titulo=titulo)
    foto = produto.foto.url if produto.foto else None
 
    return render(request, 'produtos/detalhe_produto.html', {'lm': lm, 'titulo': titulo, 'foto':foto})

def testes(request):
    return render(request, 'produtos/testes.html')