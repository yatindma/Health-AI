from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import requests
from .forms import attack_prediction_form
from predictions import utility  as util
import json
import ast
# from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
#from .models import Question


@login_required(login_url="/login/")
def index(request):
    return render(request, "predictions.html")


@login_required(login_url="/login/")
def heart_attack_prediction(request):
    #we need not to send anything from here to the HTML 
    #We just has to open normal page.
    return render(request, "heart_predict.html")
    # return HttpResponse("heart predictor is running")

@login_required(login_url="/login/")
def insurance_amount_prediction(request):
    
    
    form = attack_prediction_form(request.POST or None)
    if request.method == "POST":   # return render(request,"prediction.html")
        content = request.body
        decoded_content = json.loads(content.decode('ASCII'))
        
        
        
        age = decoded_content['age']
        sex = decoded_content["sex"]
        cp = decoded_content["cp"]           
        trestbps = decoded_content["trestbps"]
        chol = decoded_content["chol"]
        fbs = decoded_content["fbs"]
        restecg = decoded_content["restecg"]
        thalach = decoded_content["thalach"]
        exang = decoded_content["exang"]
        oldpeak = decoded_content["oldpeak"]
        slope = decoded_content["slope"]
        ca = decoded_content["ca"]
        thal = decoded_content["thal"]

        dict = {}
        dict['age'] = int(age)
        dict['sex'] = int(sex)
        dict['cp'] = int(cp)
        dict['trestbps'] = int(trestbps)
        dict['chol'] = int(chol)
        dict['fbs'] = int(fbs)
        dict['restecg'] = int(restecg)
        dict['thalach'] = int(thalach)
        dict['exang'] = int(exang)
        dict['oldpeak'] = int(oldpeak)          
        dict['slope'] = int(slope)
        dict['ca'] = int(ca)             
        dict['thal'] = int(thal)
        obj = util.Utility_()
        result = str(obj.get_heart_attack(request_obj = request,json_data = json.dumps(dict) ))[1:]
        
        y = ast.literal_eval(result)
        print(result)
        value = json.loads(y)
        response_data = {}
        
        response_data['result'] = value['Result']
        response_data['status'] = value['Status']
    return HttpResponse(json.dumps(response_data),content_type="application/json")



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
