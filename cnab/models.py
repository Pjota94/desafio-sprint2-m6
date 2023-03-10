from django.db import models


class FormData(models.Model):
    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=10)
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora_transacao = models.CharField(max_length=8)
    dono_loja = models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
