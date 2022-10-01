from rest_framework import serializers
from homeCareApp.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'especialidad', 'registro', 'usuarioMedico']