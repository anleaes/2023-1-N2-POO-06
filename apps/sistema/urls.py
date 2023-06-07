from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'sistema'

router = routers.DefaultRouter()
router.register('sistema', views.SystemViewSet, basename='sistema')

urlpatterns = [
    path('', include(router.urls) )
]
