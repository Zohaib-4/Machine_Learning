from rest_framework import serializers
from .models import DiabetesPrediction

class DiabetesPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabetesPrediction
        fields = '__all__'