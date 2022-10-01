from rest_framework import serializers
from homeCareApp.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['rol', 'username', 'password','nombres','apellidos','genero','celular','direccion','fechaNacimiento','latitud','longitud']