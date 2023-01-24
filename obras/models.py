from django.db import models
from funcionarios.models import Funcionario

class Obra(models.Model):

    objects = models.Manager()

    STATUS = (
        ("Não iniciada", "não iniciada"),
        ("Em Processo", "em processo"),
        ("Finalizada", "finalizada")
    )

    nome = models.CharField(max_length=100, null=False)
    data_inicio = models.DateField(null=True)
    valor = models.FloatField()
    parcelas = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=13, default="Não iniciada")
    regiao = models.CharField(max_length=100)
    funcionarios = models.ManyToManyField(Funcionario)

    def __str__(self):
        return self.nome