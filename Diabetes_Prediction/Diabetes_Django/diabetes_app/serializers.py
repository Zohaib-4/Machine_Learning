from rest_framework import serializers
from .models import PatientData

class DiabetesPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = '__all__'