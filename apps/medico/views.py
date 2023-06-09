from django.shortcuts import render
from .models import Medico
from rest_framework import viewsets
from .serializer import Medico

# Create your views here.

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medicot.objects.all()
    serializer_class = MedicoSerializer
