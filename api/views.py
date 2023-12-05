from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import ProdutoSerializer
from produtos.models import Produto
from django.shortcuts import render

class ProdutoView(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo', 'preco', 'media_avaliacoes', 'data_produto']
    search_fields = ['titulo', 'lm']

    #filterest_fields = ['alguma_coisa'] == Filtra por campo booleano
