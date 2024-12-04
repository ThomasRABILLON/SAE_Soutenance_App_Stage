from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import EstDansPromotion
from api.serializers.EstDansPromotionSerializer import EstDansPromotionSerializer


class EstDansPromotionViewSet(viewsets.ModelViewSet):
    queryset = EstDansPromotion.objects.all()
    serializer_class = EstDansPromotionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['etudiant', 'promotion']

# from api.views.EstDansPromoViews import EstDansPromoViewSet
# router.register(r'estdanspromo',EstDansPromoViewSet)