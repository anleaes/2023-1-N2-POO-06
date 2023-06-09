from django.shortcuts import render
from .models import Medicamento
from rest_framework import viewsets
from .serializer import MedicamentoSerializer

# Create your views here.

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
