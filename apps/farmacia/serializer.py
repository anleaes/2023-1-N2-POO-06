from .models import Farmacia
from rest_framework import serializers

class FarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = ['estoque', 'medicamento', 'lotes']