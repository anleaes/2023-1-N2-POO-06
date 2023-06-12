from django.shortcuts import render
from .models import Prescricao
from rest_framework import viewsets
from .serializer import PrescricaoSerializer


# Create your views here.

class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
