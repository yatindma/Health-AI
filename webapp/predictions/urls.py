from django.urls import path
from . import views

app_name = 'heart'
# Redirecting to multiple function from URL patterns
urlpatterns = [
    path('', views.heart_attack_prediction, name='attack_prediction'),
    path('heart_prediction_report/',views.heart_attack_report,name='heart_prediction_report')
]