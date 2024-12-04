from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import DateHoraire
from api.serializers.DateHoraireSerializer import DateHoraireSerializer

class DateHoraireViewSet(viewsets.ModelViewSet):
    queryset = DateHoraire.objects.all()
    serializer_class = DateHoraireSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_date_horaire', 'dt_date', 'heure', 'duree']  # Ajoute des filtres sur ces champs
    
#from api.view.DateHoraireViews import DateHoraireViewSet
#router.register(r'datehoraire', DateHoraireViewSet)