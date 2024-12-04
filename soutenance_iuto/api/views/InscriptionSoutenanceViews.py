from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import InscriptionSoutenance
from api.serializers.InscriptionSoutenanceSerializer import InscriptionSoutenanceSerializer

class InscriptionSoutenanceViewSet(viewsets.ModelViewSet):
    queryset = InscriptionSoutenance.objects.all()
    serializer_class = InscriptionSoutenanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['soutenance', 'prof']  # Ajoute des filtres sur ces champs
    
# from api.view.InscriptionSoutenanceViews import InscriptionSoutenanceViewSet
# router.register(r'inscriptionsoutenance', InscriptionSoutenanceViewSet)