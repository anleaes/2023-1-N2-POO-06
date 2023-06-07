from .models import system
from rest_framework import serializers

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = sistema
        fields = '__all__'

        # Para chamar todos os atributos:
        # fields = '__all__'

        # Para chamar somentes os atributos de interesse:
        # fields = ['id','created_on', 'updated_on', 'name', 'description']
