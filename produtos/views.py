from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from produtos.models import Produto
from produtos.conteudo.search_data import *
from produtos.conteudo.format_values import format_real
from .forms import ProdutoForm
from urllib.parse import unquote
from django.core.paginator import Paginator

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a página.')
        return redirect('login')
    else:
        produto = Produto.objects.order_by("-data_produto")
        p = Paginator(Produto.objects.all(), 10)
        page = request.GET.get('page')
        dados_organizados = p.get_page(page)
        nums = "a" * dados_organizados.paginator.num_pages

        return render(request, 'produtos/index.html',{"cards": produto, 'dados_organizados': dados_organizados, 'nums':nums})

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

            html_element = requisition(url).find('h1', class_='product-title align-left color-text')
                
            if html_element:
                title, lm = get_title_and_lm(url, html_element)

                html_price = requisition(url).find('div',class_='product-price-tag')
                formated_price = find_price(html_price)
                preco = format_real(formated_price)
                preco = float(preco)

                review, average_review = get_review(lm)

                foto = get_image(url)

                #info_produto = get_info_produto(url)

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

    p = Paginator(Produto.objects.all(), 10)
    page = request.GET.get('page')
    dados_organizados = p.get_page(page)
    nums = "i" * dados_organizados.paginator.num_pages

    return render(request, 'produtos/dados.html', {'dados': dados, 'dados_organizados': dados_organizados, 'nums': nums})

def detalhe_produto(request):
    lm = request.GET.get('lm')
    titulo = unquote(request.GET.get('titulo'))
    produto = Produto.objects.get(lm=lm, titulo=titulo)
    foto = produto.foto.url if produto.foto else None

    return render(request, 'produtos/detalhe_produto.html', {'lm': lm, 'titulo': titulo, 'foto':foto})

def testes(request):
    return render(request, 'produtos/testes.html')

