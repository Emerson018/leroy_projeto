from django.urls import path
from produtos.views import index, detalhe_produto, buscar, lista, dados

urlpatterns = [
    path('', index, name='index'),
    path('detalhe_produto', detalhe_produto, name='detalhe_produto'),
    path('buscar', buscar, name='buscar'),
    path('lista', lista, name='lista'),
    path('dados', dados, name='dados'),
]