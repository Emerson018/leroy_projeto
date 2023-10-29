from django.shortcuts import render



def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org/NASA"},
        2: {"nome": "Galáxia NGC",
        "legenda": "nasa.org/NASA"}
    }

    return render(request, 'produtos/index.html',{"cards": dados})

def imagem(request):
    return render(request, 'produtos/imagem.html')