from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('diagnoses/', views.diagnose, name="diagnoses"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('assessment/', views.regguardian, name="assessment"),
    path('assessment/submit/', views.submitAssessment, name="assessment/submit"),
]