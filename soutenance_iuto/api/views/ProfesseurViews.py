from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Professeur
from api.serializers.ProfesseurSerializer import ProfesseurSerializer

class ProfesseurViewSet(viewsets.ModelViewSet):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_prof', 'nom_prof']