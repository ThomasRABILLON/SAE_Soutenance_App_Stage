from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Etudiant
from api.serializers.EtudiantSerializer import EtudiantSerializer

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_etu', 'num_etu']