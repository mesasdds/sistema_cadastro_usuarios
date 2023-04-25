from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) ##criação primary key
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

