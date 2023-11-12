from django.urls import path
from produtos.views import index, item, buscar, lista, dados

urlpatterns = [
    path('', index, name='index'),
    path('item/', item, name='item'),
    path('buscar', buscar, name='buscar'),
    path('lista', lista, name='lista'),
    path('dados', dados, name='dados'),
]