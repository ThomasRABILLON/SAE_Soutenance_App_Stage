from rest_framework import serializers
from ..models import TuteurPro

"""Classe permettant de sérialiser les données d'un tuteur professionnel"""
class TuteurProSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuteurPro
        fields = '__all__'