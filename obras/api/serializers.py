from rest_framework import serializers
from obras import models
from funcionarios.api.serializers import FuncionarioSerializer

class ObraSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Obra
        fields = "__all__"