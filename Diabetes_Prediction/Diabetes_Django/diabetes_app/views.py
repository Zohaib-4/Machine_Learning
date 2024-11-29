from rest_framework import viewsets
from .models import PatientData
# from .serializers import DiabetesPredictionSerializer
from rest_framework.response import Response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import status

def prediction(request):
    # error_message = ""
    if request.method == 'POST':
        pregnancies = request.POST.get('pregnancies')
        glucose = request.POST.get('glucose')
        blood_pressure = request.POST.get('blood_pressure')
        skin_thickness = request.POST.get('skin_thickness')
        insulin = request.POST.get('insulin')
        bmi = request.POST.get('bmi')
        diabetes_pedigree_function = request.POST.get('diabetes_pedigree_function')
        age = request.POST.get('age')
        
        print(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)


        PatientData.objects.create(
            pregnancies=pregnancies,
            glucose=glucose,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin=insulin,
            bmi=bmi,
            diabetes_pedigree_function=diabetes_pedigree_function,
            age=age
        )

        return redirect('success')

    return render(request, 'index.html')
    # return render(request, 'index.html', {'error_message': error_message})



def success(request):
    return HttpResponse("All set good to go")