"""homeCareProject URL Configuration

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
from django.urls import path
from homeCareApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', views.usuarioView.UsuarioListView.as_view()),
    path('usuario/<int:pk>/', views.usuarioView.UsuarioRetrieveUpdateDeleteView.as_view()),
    path('medico/', views.medicoView.MedicoListCreateView.as_view()),
    path('medico/<int:pk>/', views.medicoView.MedicoRetrieveUpdateView.as_view()),
    path('paciente/', views.pacienteView.MedicoListCreateView.as_view()),
    path('paciente/<int:pk>/', views.pacienteView.MedicoRetrieveUpdateView.as_view()),
    path('familiar/', views.familiarView.MedicoListCreateView.as_view()),
    path('familiar/<int:pk>/', views.familiarView.MedicoRetrieveUpdateView.as_view()),
    path('enfermero/', views.enfermeroView.MedicoListCreateView.as_view()),
    path('enfermero/<int:pk>/', views.enfermeroView.MedicoRetrieveUpdateView.as_view()),
]
