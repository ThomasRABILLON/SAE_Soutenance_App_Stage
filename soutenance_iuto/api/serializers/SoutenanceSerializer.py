from rest_framework import serializers
from api.models import Soutenance

"""Class permettant de sérialser les données d'une soutenance"""
class SoutenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soutenance
        fields = '__all__'
        