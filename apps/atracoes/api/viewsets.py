from rest_framework.viewsets import ModelViewSet
from apps.atracoes.models import Atracao
from .serializers import AtracaoSerializer
from rest_framework import filters


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome', 'descricao')


