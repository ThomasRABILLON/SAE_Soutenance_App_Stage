from rest_framework import serializers
from api.models import Secretaire

"""Class permettant de sérialser les données d'un secrétaire"""
class SecretaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretaire
        fields = '__all__'