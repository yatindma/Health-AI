from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient

from django.forms import ModelForm

from .services import PatientService



class PatientsForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['id','patientuid', 'first_name', 'middle_name','last_name','gender','dob','phone','email','street1','street2','city','state','country','zipcode']

patientservice=PatientService()	

@login_required(login_url="/login/")
def index(request):

    return render(request, "index.html")
	
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

		
def patient_list(request):
    patients = Patient.objects.all()
    data = {}
    data['object_list'] = patients
    return render(request, "patient_list.html", data)

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method=='GET':
        patient.delete()
        return redirect("/patients/patient_list.html")
    return render(request, "patient_list.html")
	
def patient_create(request):
    form = PatientsForm(request.POST or None)
    if form.is_valid() and not(patientservice.isduplicatepateint()):
        form.save()
        return redirect("/patients/patient_list.html")
    return render(request, "patient_create.html")	

# Handles bulk upload of patients 
# Data must be supplied in defined CSV template
# Use panda library to read and push the CSV file to database 	

def patient_upload(request):
    
    if request.method=='POST':
        
        # Logic for reading CSV file and pushing to DB
        
        return redirect("/patients/patient_list.html")
    return render(request, "patient_upload.html")	
