from django.urls import path

from . import views

app_name = 'predictions '
urlpatterns = [
    path('', views.index, name='index'),
    path('attack_prediction/', views.heart_attack_prediction, name='attack_prediction'),
    path('attack_prediction/insurance_prediction/',views.insurance_amount_prediction,name='insurance_prediction')
]