from django.db import models
from .usuario import Usuario

class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    usuarioFamiliar = models.ForeignKey(Usuario, related_name='familiar', on_delete=models.CASCADE)
    email = models.EmailField('Email', max_length = 100)