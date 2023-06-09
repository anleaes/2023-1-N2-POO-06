from django.shortcuts import render
from .models import Prontuario
from rest_framework import viewsets
from .serializer import ProntuarioSerializer

# Create your views here.

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer

