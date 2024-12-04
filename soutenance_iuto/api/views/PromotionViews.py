from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Promotion
from api.serializers.PromotionSerializer import PromotionSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_promo', 'annee_promo', 'filiere_promo']

# from api.views.PromotionViews import PromotionViewSet
# router.register(r'promotion',PromotionViewSet)