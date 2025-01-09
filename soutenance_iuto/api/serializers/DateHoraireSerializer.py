from rest_framework import serializers
from api.models import DateHoraire

"""Class permettant de sérialser les données d'une date et d'un horaire"""
class DateHoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateHoraire
        fields = '__all__'