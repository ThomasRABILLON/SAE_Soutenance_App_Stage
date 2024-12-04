from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from api.models import EstResponsable
from api.serializers.EstResponsableSerializer import EstResponsableSerializer


class EstResponsableViewSet(viewsets.ModelViewSet):
    queryset = EstResponsable.objects.all()
    serializer_class = EstResponsableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['professeur', 'promotion']

# from api.views.EstResponsableViews import EstResponsableViewSet
# router.register(r'estresponsable',EstResponsableViewSet)