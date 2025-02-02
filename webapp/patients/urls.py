from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.patient_list, name='patient_list'),
	
	path('patients', views.patient_list, name='patient_list'),
	path('patient_list.html', views.patient_list, name='patient_list'),
	path('patient_delete/<int:pk>', views.patient_delete, name='patient_delete'),
	path('patient_create.html', views.patient_create, name='patient_create'),
	path('patient_upload.html', views.patient_upload, name='patient_upload'),
	path('patient_update/<int:pk>', views.patient_update, name='patient_update'),
]