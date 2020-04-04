from django.db import models
# Create your models here.
class Registrado(models.Model):
    usuario = models.CharField(max_length = 70,unique = True)
    password = models.CharField(max_length=140)
    correo=models.EmailField(unique = True)
    def __str__(self):
        return self.usuario

class Resena(models.Model):
    usuario = models.CharField(max_length = 70)
    calificacion = models.IntegerField()
    resena = models.CharField(max_length=4000)
    libro_titulo = models.CharField(max_length = 70)
    def __str__(self):
        return self.usuario

class Libro(models.Model):
    isbn= models.CharField(primary_key=True,max_length = 70)
    title = models.CharField(max_length = 70)
    author = models.CharField(max_length = 70)
    year = models.IntegerField()
    def __str__(self):
        return self.title
