from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Salle
from api.serializers.SalleSerializer import SalleSerializer


class SalleViewSet(viewsets.ModelViewSet):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_salle', 'nom_salle']

# from api.views.SalleViews import SalleViewSet
# router.register(r'salle',SalleViewSet)