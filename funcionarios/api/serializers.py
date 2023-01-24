from rest_framework import serializers
from funcionarios import models

class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Funcionario
        fields = "__all__"
