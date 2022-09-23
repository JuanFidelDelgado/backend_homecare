from django.db import models

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    oximetria = models.FloatField('Oximetria', default=0)
    fCardiaca = models.FloatField('FCardiaca', default=0)
    fRespiratoria = models.FloatField('FRespiratoria', default=0)
    temperatura = models.FloatField('Temperatura', default=0)
    presionArterial = models.FloatField('PresionArterial', default=0)
    glicemias = models.FloatField('Glicemias', default=0)
    diagnostico = models.CharField('Diagnostico', max_length=256)
    sugerencia = models.CharField('Sugerencia', max_length=256)
