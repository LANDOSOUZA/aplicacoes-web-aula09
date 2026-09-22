from rest_framework import serializers
from .models import Ativo, HistoricoMovimentacao


class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ativo
        fields = [
            "id",
            "tipo",
            "descricao",
            "numero_patrimonio",
            "codigo_qr",
            "sala",
            "status",
            "latitude",
            "longitude",
            "criado_em",
        ]


class HistoricoMovimentacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoMovimentacao
        fields = [
            "id",
            "ativo",
            "sala_origem",
            "sala_destino",
            "data_movimentacao",
            "observacao",
        ]