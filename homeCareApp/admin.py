from django.contrib import admin

from .models.usuario import Usuario
from .models.medico import Medico
from .models.familiar import Familiar
from .models.enfermero import Enfermero
from .models.paciente import Paciente
from .models.historiaClinica import HistoriaClinica

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Familiar)
admin.site.register(Enfermero)
admin.site.register(Paciente)
admin.site.register(HistoriaClinica)