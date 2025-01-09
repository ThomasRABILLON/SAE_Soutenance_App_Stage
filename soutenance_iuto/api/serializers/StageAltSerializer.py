from rest_framework import serializers
from api.models import StageAlt

"""Class permettant de sérialser les données d'un stage ou d'une alternance"""
class StageAltSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageAlt
        fields = '__all__'