from django.db import models

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    idade = models.IntegerField()
