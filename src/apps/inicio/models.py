from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    identificacion = models.CharField('Identificación', max_length=20)
    foto = models.ImageField(upload_to='user/pictures', blank=True, null=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username


class Board(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    ESTADO = (
        ('PRIVADO', 'PRIVADO'),
        ('PUBLICO', 'PUBLICO'),
    )
    nombre = models.CharField('Nombre del Tablero', max_length=50)
    estado = models.CharField('Estado', max_length=10, choices=ESTADO, default='PRIVADO')

    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'

    def __str__(self):
        return "El usuario %s crea %s" % (self.propietario, self.nombre)


class Idea(models.Model):
    board  = models.ForeignKey(Board,related_name='ideas', on_delete=models.CASCADE)
    ESTADO = (
        ('PRIVADO', 'PRIVADO'),
        ('PUBLICO', 'PUBLICO'),
    )
    nombre = models.TextField('Nombre de la Idea')
    estado = models.CharField('Estado', max_length=10, choices=ESTADO, default='PRIVADO')

    def __str__(self):
        return self.nombre