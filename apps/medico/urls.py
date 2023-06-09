from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'medico'

router = routers.DefaultRouter()
router.register('medico', views.MedicoViewSet, basename='medico')

urlpatterns = [
    path('', include(router.urls) )
]
