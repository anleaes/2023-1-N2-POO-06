from .models import Paciente
from rest_framework import serializers

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['name', 'cpf', 'data_nascimento_', 'endereco', 'historico', 'sexo']
