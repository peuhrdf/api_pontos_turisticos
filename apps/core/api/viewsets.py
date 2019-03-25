from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.filters import SearchFilter


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return PontoTuristico.objects.all()

    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # @action(methods=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
