from django.shortcuts import render

# Create your views here.
from .models import sistema
from rest_framework import viewsets
from .serializer import sistemaSerializer

# Após o comentario "# Create your views here." e crie as views "sistema".

class sistemaViewSet(viewsets.ModelViewSet):
    queryset = sistema.objects.all()
    serializer_class = sistemaSerializer  