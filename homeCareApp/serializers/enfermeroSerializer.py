from rest_framework import serializers
from homeCareApp.models.enfermero import Enfermero

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['id', 'area', 'auxiliar', 'usuarioEnfermero']