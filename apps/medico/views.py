from django.shortcuts import render
from .models import Medico
from rest_framework import viewsets
from .serializer import MedicoSerializer

# Create your views here.

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
