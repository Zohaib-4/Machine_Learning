from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'predictions', views.DiabetesPredictionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]