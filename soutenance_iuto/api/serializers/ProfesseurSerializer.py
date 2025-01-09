from rest_framework import serializers
from ..models import Professeur

"""Classe permettant de sérialiser les données d'un professeur"""
class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'