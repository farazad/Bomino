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

class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SumationRepo
        fields = ['result']

    def to_representation(self, instance):
        return super().to_representation(instance)