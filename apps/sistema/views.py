from django.shortcuts import render

from .models import Sistema
from rest_framework import viewsets
from .serializer import SistemaSerializer


# Create your views here.

class SistemaViewSet(viewsets.ModelViewSet):
    queryset = Sistema.objects.all()
    serializer_class = SistemaSerializer
