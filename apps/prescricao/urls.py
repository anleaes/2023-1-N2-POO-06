from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'prescricao'

router = routers.DefaultRouter()
router.register('prescricao', views.PrescricaoViewSet, basename='prescricao')

urlpatterns = [
    path('', include(router.urls))
]
