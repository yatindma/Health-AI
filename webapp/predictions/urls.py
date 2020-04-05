from django.urls import path
from . import views

app_name = 'heart'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.heart_attack_prediction, name='attack_prediction'),
    path('heart_prediction_report/',views.heart_attack_report,name='heart_prediction_report')
]
#path('attack_prediction/', views.heart_attack_prediction, name='attack_prediction'),