from django.db import models

class PatientData(models.Model):
    pregnancies = models.PositiveIntegerField(help_text="Number of pregnancies")
    glucose = models.PositiveIntegerField(help_text="Plasma glucose concentration (mg/dL)")
    blood_pressure = models.PositiveIntegerField(help_text="Diastolic blood pressure (mm Hg)")
    skin_thickness = models.PositiveIntegerField(help_text="Triceps skin fold thickness (mm)")
    insulin = models.PositiveIntegerField(help_text="2-Hour serum insulin (mu U/ml)")
    bmi = models.FloatField(help_text="Body Mass Index (weight in kg/(height in m)^2)")
    diabetes_pedigree_function = models.FloatField(help_text="Diabetes pedigree function score")
    age = models.PositiveIntegerField(help_text="Age of the patient (years)")
    outcome = models.BooleanField(help_text="Diabetes outcome: 0 (No), 1 (Yes)")

    def __str__(self):
        return f"Patient {self.id} - Outcome: {'Diabetes' if self.outcome else 'No Diabetes'}"