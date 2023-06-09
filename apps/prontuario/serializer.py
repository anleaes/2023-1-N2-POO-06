from .models import Prontuario
from rest_framework import serializers

class ProntuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prontuario
        fields = ['paciente', 'data_criacao', 'sintomas', 'diagnostico']
