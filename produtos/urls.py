from django.urls import path
from produtos.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
]