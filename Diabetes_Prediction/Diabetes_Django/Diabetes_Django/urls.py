from django.urls import path, include
from rest_framework import routers
from diabetes_app import views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
]