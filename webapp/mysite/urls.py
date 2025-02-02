"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path , re_path
from django.views.generic import TemplateView
from patients import views

urlpatterns = [
    path("", include("authentication.urls")),
    path('heart_attack_prediction/', include('predictions.urls')),
	path('hospital/', include('hospital.urls')),
    path('predictions/', include('predictions.urls')),
    path('patients/', include('patients.urls')),
    path('admin/', admin.site.urls),
	
	
	# Matches any html file 
    re_path(r'^.*\.html', views.pages, name='pages'),

	path('', views.index, name='home'),
]
