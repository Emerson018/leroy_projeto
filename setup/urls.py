from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.ProdutoView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produtos.urls')),
    path('', include('usuarios.urls')),
    path('', include('api.urls')),
    path('api/', include(router.urls))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
