from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.patient_list, name='patient_list'),
	
	path('patients', views.patient_list, name='patient_list'),
	path('patient_delete/<int:pk>', views.patient_delete, name='patient_delete'),
	path('patient_update/<int:id>', views.patient_update, name='patient_update'),
	path('patient_create.html', views.patient_create, name='patient_create'),
	#path('patient', views.patient_detail, name='patient_detail'),
    #path('patient/<int:pk>', views.PatientDetail.as_view(), name='patient_detail'),
    #path('create', views.PatientCreate.as_view(), name='patient_create'),
    #path('update/<int:pk>', views.PatientUpdate.as_view(), name='patient_update'),

]