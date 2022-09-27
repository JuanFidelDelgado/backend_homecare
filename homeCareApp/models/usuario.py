from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    rol = models.CharField('Rol', max_length=20)
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    genero = models.CharField('Genero', max_length=20)
    celular = models.CharField('Celular', max_length=50)
    direccion = models.CharField('Direccion', max_length=50)
    ciudad = models.CharField('Ciudad', max_length=50)
    fechaNacimiento = models.DateField()
    latitud = models.CharField('Latitud', max_length=50)
    longitud = models.CharField('Longitud', max_length=50)
    
    
    username = models.CharField('Username', max_length = 20, unique=True)
    password = models.CharField('Password', max_length = 256)
    
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'