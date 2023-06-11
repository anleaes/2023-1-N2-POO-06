from .models import Medicamento
from rest_framework import serializers

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = ['nome', 'numero_lote', 'validade']
