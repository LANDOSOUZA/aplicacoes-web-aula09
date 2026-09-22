from django.contrib import admin
from .models import Ativo, HistoricoMovimentacao


@admin.register(Ativo)
class AtivoAdmin(admin.ModelAdmin):
    list_display = ("id", "tipo", "numero_patrimonio", "sala", "status", "criado_em")
    search_fields = ("tipo", "numero_patrimonio", "codigo_qr")
    list_filter = ("status", "sala")


@admin.register(HistoricoMovimentacao)
class HistoricoMovimentacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "ativo", "sala_destino", "data_movimentacao")
    search_fields = ("ativo__tipo", "ativo__numero_patrimonio")