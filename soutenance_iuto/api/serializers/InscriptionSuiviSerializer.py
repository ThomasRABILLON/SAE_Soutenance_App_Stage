from rest_framework import serializers
from api.models import InscriptionSuivi

"""Class permettant de sérialser les données d'une inscription à un suivi"""
class InscriptionSuiviSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionSuivi
        fields = '__all__'