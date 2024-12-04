from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import InscriptionSuivi
from api.serializers.InscriptionSuiviSerializer import InscriptionSuiviSerializer

class InscriptionSuiviViewSet(viewsets.ModelViewSet):
    queryset = InscriptionSuivi.objects.all()
    serializer_class = InscriptionSuiviSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['stg_alt', 'prof']
