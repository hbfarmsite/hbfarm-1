from django.db import models

class Ovo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)

