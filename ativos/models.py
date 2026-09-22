from django.db import models


class Ativo(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('manutencao', 'Em manutenção'),
        ('inativo', 'Inativo'),
    ]

    tipo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    codigo_qr = models.CharField(max_length=100, unique=True)
    sala = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.numero_patrimonio}"


class HistoricoMovimentacao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name='movimentacoes')
    sala_origem = models.CharField(max_length=100, blank=True)
    sala_destino = models.CharField(max_length=100)
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True)

    def __str__(self):
        return f"{self.ativo} → {self.sala_destino} ({self.data_movimentacao:%d/%m/%Y})"