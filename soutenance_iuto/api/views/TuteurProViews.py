from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import TuteurPro
from api.serializers.TuteurProSerializer import TuteurProSerializer

class TuteurProSerializerSet(viewsets.ModelViewSet):
    queryset = TuteurPro.objects.all()
    serializer_class = TuteurProSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_tut_pro', 'nom_tut_pro']  # Ajoute des filtres sur ces champs