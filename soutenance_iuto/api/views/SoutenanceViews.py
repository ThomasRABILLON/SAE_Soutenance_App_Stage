from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Soutenance
from api.serializers.SoutenanceSerializer import SoutenanceSerializer

class SoutenanceViewSet(viewsets.ModelViewSet):
    queryset = Soutenance.objects.all()
    serializer_class = SoutenanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_sout', 'stg_alt', 'horaire', 'salle', 'prof_candide']  # Ajoute des filtres sur ces champs
    
# from api.view.SoutenanceViews import SoutenanceViewSet
# router.register(r'soutenance', SoutenanceViewSet)