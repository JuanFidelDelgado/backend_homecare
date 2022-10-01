from rest_framework import serializers
from homeCareApp.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ['id', 'email', 'usuarioFamiliar']