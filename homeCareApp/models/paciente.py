from django.db import models

from .usuario import Usuario
from .medico import Medico
from .familiar import Familiar
from .enfermero import Enfermero
#from .historiaClinica import HistoriaClinica

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    usuarioPaciente = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE)
    usuarioMedico = models.ForeignKey(Medico, related_name='paciente', on_delete=models.CASCADE)
    usuarioFamiliar = models.ForeignKey(Familiar, related_name='paciente', on_delete=models.CASCADE)
    usuarioEnfermero = models.ForeignKey(Enfermero, related_name='paciente', on_delete=models.CASCADE)
    #historiaClinica = models.ForeignKey(HistoriaClinica, related_name='paciente', on_delete=models.CASCADE)