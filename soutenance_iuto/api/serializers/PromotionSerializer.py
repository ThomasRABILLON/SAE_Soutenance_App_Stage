from rest_framework import serializers
from ..models import Promotion

"""Classe permettant de sérialiser les données d'une promotion"""
class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'