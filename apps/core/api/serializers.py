from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from apps.core.models import PontoTuristico
from apps.atracoes.api.serializers import AtracaoSerializer
from apps.comentarios.api.serializers import ComentarioSerializer
from apps.avaliacoes.api.serializers import AvaliacaoSerializer
from apps.enderecos.api.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes',
                  'comentarios', 'avaliacoes', 'endereco','descricao_completa')

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
