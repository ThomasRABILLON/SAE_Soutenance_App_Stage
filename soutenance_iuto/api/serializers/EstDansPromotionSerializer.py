from rest_framework import serializers
from ..models import EstDansPromotion

"""Classe permettant de sérialiser les données d'un étudiant dans une promotion"""
class EstDansPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstDansPromotion
        fields = '__all__'