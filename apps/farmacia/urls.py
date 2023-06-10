from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'farmacia'

router = routers.DefaultRouter()
router.register('farmacia', views.FarmaciaViewSet, basename='farmacia')

urlpatterns = [
    path('', include(router.urls) )
]
