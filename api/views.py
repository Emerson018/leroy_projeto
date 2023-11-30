from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProdutoSerializer
from produtos.models import Produto

class ProdutoView(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
