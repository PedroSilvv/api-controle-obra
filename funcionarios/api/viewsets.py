from rest_framework import viewsets
from funcionarios.api import serializers
from funcionarios.models import Funcionario

class FuncionarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FuncionarioSerializer
    queryset = Funcionario.objects.all()

