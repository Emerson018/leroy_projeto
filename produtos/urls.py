from django.urls import path
from produtos.views import index, detalhe_produto, buscar, lista, dados, testes, dashboard, admin_dashboard, admin_dashboard2

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('detalhe_produto', detalhe_produto, name='detalhe_produto'),
    path('buscar', buscar, name='buscar'),
    path('lista', lista, name='lista'),
    path('dados', dados, name='dados'),
    path('testes',testes, name='testes' ),
    path('dashboard', dashboard, name='dashboard'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard2', admin_dashboard2, name='admin_dashboard2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)