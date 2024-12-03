from rest_framework import serializers
from api.models import DateHoriare

"""Class permettant de sérialser les données d'une date et d'un horaire"""
class DateHoriareSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateHoriare
        fields = '__all__'