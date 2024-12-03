from rest_framework import serializers
from ..models import Etudiant

"""Classe permettant de sérialiser les données d'un étudiant"""
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'