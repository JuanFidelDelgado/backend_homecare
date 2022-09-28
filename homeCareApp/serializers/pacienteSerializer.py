from rest_framework import serializers
from homeCareApp.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Paciente
        fields= ['id', 'area', 'auxiliar', 'usuarioEnfermero']