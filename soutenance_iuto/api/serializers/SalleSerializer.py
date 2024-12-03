from rest_framework import serializers
from api.models import Salle

"""Class permettant de sérialser les données d'une salle"""
class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = '__all__'