from rest_framework import serializers
from ..models import Entreprise

"""Classe permettant de sérialiser les données d'une entreprise"""
class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'