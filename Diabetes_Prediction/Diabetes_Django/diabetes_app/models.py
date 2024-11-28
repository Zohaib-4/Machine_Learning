from django.db import models

class PatientData(models.Model):
    pregnancies = models.PositiveIntegerField()
    glucose = models.PositiveIntegerField()
    blood_pressure = models.PositiveIntegerField()
    skin_thickness = models.PositiveIntegerField()
    insulin = models.PositiveIntegerField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.PositiveIntegerField()
    outcome = models.BooleanField()

    def __str__(self):
        return f"Patient {self.id} - Outcome: {'Diabetes' if self.outcome else 'No Diabetes'}"