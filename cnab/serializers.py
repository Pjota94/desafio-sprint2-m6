from rest_framework import serializers

from .models import FormData

class FormSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = [
            'tipo',
            'data',
            'valor',
            'cpf',
            'cartao',
            'hora_transacao',
            'dono_loja',
            'nome_loja'
        ]