from .models import Prescricao
from rest_framework import serializers


class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = '__all__'
