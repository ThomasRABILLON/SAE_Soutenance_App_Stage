from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Secretaire
from api.serializers.SecretaireSerializer import SecretaireSerializer

class SecretaireViewSet(viewsets.ModelViewSet):
    queryset = Secretaire.objects.all()
    serializer_class = SecretaireSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_sec', 'prenom_sec']  # Ajoute des filtres sur ces champs

# from api.views.SecretaireView import SecretaireViewSet
# router.register(r'professeurs',SecretaireViewSet)