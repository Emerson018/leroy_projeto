from django.shortcuts import render, redirect
from django.contrib import messages
from produtos.models import Produto
from produtos.conteudo.search_data import find_price, get_review, requisition, get_image
from produtos.conteudo.format_values import format_real, format_cents
from .forms import ProdutoForm

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
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            produtos = produtos.filter(titulo__icontains=nome_a_buscar)

    return render(request, 'produtos/buscar.html', {"cards": produtos})

def lista(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['link']
            
            if 'leroymerlin.com.br' not in url:
                messages.error(request, 'Formulário inválido. Certifique-se de inserir o link correto.')
                return redirect('lista')

            title_element = requisition(url).find('h1', class_='product-title align-left color-text')
                
            if title_element:
                title = title_element.text.replace('\n', '')
                barcode = requisition(url).find('div', class_='badge product-code badge-product-code').text
                lm = ''
                for caractere in barcode:
                    if caractere.isdigit():
                        lm += caractere

                prod_price = requisition(url).find('div',class_='product-price-tag')

                price = find_price(prod_price)
                reais = format_real(price)
                centavos = format_cents(price) 
                preco = (reais + centavos)
                review, average_review = get_review(lm)
                #NAO ESTÁ FUNCIONANDO, TEM Q VER DPOIS
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
                            {'title': title, 'lm': lm, 'preco':preco, 'url': url, 'avaliacoes': review, 'media_avaliacoes': average_review, 'foto': foto})
            
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
    titulo = request.GET.get('titulo')
    
    produto = Produto.objects.get(lm=lm, titulo=titulo)

    foto = produto.foto.url if produto.foto else None

    return render(request, 'produtos/detalhe_produto.html', {'lm': lm, 'titulo': titulo, 'foto':foto})