from rest_framework import serializers
from ..models import EstResponsable

"""Classe permettant de sérialiser les données d'un responsable"""
class EstResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstResponsable
        fields = '__all__'