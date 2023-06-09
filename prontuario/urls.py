from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'prontuario'

router = routers.DefaultRouter()
router.register('prontuario', views.ProntuarioViewSet, basename='prontuario')

urlpatterns = [
    path('', include(router.urls) )
]
