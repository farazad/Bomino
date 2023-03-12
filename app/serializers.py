from rest_framework import serializers
from app.models import SumationRepo

class SumationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SumationRepo
        fields = ['a', 'b', 'result']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SumationRepo
        fields = ['a', 'b']