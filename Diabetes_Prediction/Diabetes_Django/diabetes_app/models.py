from django.db import models

class DiabetesPrediction(models.Model):
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    # ... other fields as needed

    def __str__(self):
        return f"Prediction for {self.id}"