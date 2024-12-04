from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import StageAlt
from api.serializers.StageAltSerializer import StageAltSerializer


class StageAltViewSet(viewsets.ModelViewSet):
    queryset = StageAlt.objects.all()
    serializer_class = StageAltSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_stg_alt', 'titre_stg_alt', 'theme_stg_alt', 'intitule_stg_alt', 'dt_date_debut_stg_alt', 'dt_date_fin_stg_alt', 'duree_stg_alt', 'entreprise', 'tuteur_pro', 'tuteur_univ', 'etudiant']

# from api.views.StageAltViews import StageAltViewSet
# router.register(r'stagealt',StageAltViewSet)