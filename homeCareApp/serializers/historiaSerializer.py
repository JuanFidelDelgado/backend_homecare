from rest_framework import serializers
from homeCareApp.models.historiaClinica import HistoriaClinica

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ['id', 'oximetria', 'fCardiaca', 'fRespiratoria', 'temperatura', 'presionArterial', 'glicemias', 'diagnostico', 'sugerencia', 'usuarioPaciente']