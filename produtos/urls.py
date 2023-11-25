from django.urls import path
from produtos.views import index, detalhe_produto, buscar, lista, dados

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('detalhe_produto', detalhe_produto, name='detalhe_produto'),
    path('buscar', buscar, name='buscar'),
    path('lista', lista, name='lista'),
    path('dados', dados, name='dados'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)