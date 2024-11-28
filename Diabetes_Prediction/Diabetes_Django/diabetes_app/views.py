from rest_framework import viewsets
from .models import PatientData
from .serializers import DiabetesPredictionSerializer
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status

class DiabetesPredictionViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = DiabetesPredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Here, you'd integrate your machine learning model to predict the outcome
            # Based on the input data, calculate the prediction
            prediction = 1  # Replace with your actual prediction logic

            return Response({'prediction': prediction}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


    def members(request):
        return HttpResponse("Hello world!")