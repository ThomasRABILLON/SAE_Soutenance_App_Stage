from rest_framework import serializers
from api.models import InscriptionSoutenance

"""Class permettant de sérialser les données d'une inscription à une soutenance"""
class InscriptionSoutenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionSoutenance
        fields = '__all__'