from django.urls import path
from produtos.views import index, imagem, buscar, lista, dados

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('lista', lista, name='lista'),
    path('dados', dados, name='dados'),
]