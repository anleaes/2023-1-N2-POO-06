"""prontuarioapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sistema/', include(('sistema.urls', 'sistema'), namespace='sistema')),
    path('paciente/', include(('paciente.urls', 'paciente'), namespace='paciente')),
    path('medico/', include(('medico.urls', 'medico'), namespace='medico'))
#     path('farmacia/', include(('farmacia.urls', 'farmacia'), namespace='farmacia')),
#     path('prontuario/', include(('prontuario.urls', 'prontuario'), namespace='prontuario')),
#     path('medicamento/', include(('medicamento.urls', 'medicamento'), namespace='medicamento')),
#     path('prescricao/', include(('prescricao.urls', 'prescricao'), namespace='prescricao'))   
]

