from django.shortcuts import render
from .models import Farmacia
from rest_framework import viewsets
from .serializer import FarmaciaSerializer

# Create your views here.

class FarmaciaViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer