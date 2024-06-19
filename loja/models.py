from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    id_sessao = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


class Produto(models.Model):
    ...
