from rest_framework import viewsets
from obras.api import serializers
from obras.models import Obra

class ObraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObraSerializer
    queryset = Obra.objects.all()

