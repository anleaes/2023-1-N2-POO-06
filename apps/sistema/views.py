from django.shortcuts import render

from .models import System
from rest_framework import viewsets
from .serializer import SystemSerializer


# Create your views here.

class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
