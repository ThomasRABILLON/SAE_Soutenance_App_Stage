from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Entreprise
from api.serializers.EntrepriseSerializer import EntrepriseSerializer


class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_etp', 'nom_etp']  # Ajoute des filtres sur ces champs