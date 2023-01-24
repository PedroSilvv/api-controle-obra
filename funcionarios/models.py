from django.db import models

class Funcionario(models.Model):

    objects = models.Manager()

    nome = models.CharField(max_length=100, null=False)
    registrado = models.BooleanField(default=True)

    def __str__(self):
        return self.nome