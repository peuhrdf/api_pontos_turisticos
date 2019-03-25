from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from apps.core.api.viewsets import PontoTuristicoViewSet
from apps.atracoes.api.viewsets import AtracaoViewSet
from apps.enderecos.api.viewsets import EnderecoViewSet
from apps.avaliacoes.api.viewsets import AvaliacaoViewSet
from apps.comentarios.api.viewsets import ComentarioViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = routers.DefaultRouter()

router.register('pontoturistico', PontoTuristicoViewSet, base_name='PontoTuristico')
router.register('atracoes', AtracaoViewSet)
router.register('enderecos', EnderecoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('comentario', ComentarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
