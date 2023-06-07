from .models import Sistema
from rest_framework import serializers

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = '__all__'

        # Para chamar todos os atributos:
        # fields = '__all__'

        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
