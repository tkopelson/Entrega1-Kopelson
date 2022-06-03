from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=30)
    area = models.CharField(max_length=30)


class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)

class Graduados(models.Model):
    nombre = models.CharField(max_length=40)
    nota = models.IntegerField()



    