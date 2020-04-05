from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import requests
from .forms import attack_prediction_form
from predictions import utility as util
import json
import ast
from django.core import serializers
# from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . import models
from django.forms.models import model_to_dict
#from .models import Question


@login_required(login_url="/login/")
def index(request):
    return render(request, "predictions.html")


@login_required(login_url="/login/")
def heart_attack_prediction(request):
    # we need not to send anything from here to the HTML
    # We just has to open normal page.
    return render(request, "heart_predict.html")
    # return HttpResponse("heart predictor is running")


@login_required(login_url="/login/")
def heart_attack_report(request):

    # form = attack_prediction_form(request.POST or None)
    if request.method == "POST":   # return render(request,"prediction.html")
        content = request.body
        decoded_content = json.loads(content.decode('ASCII'))

        heart_object = models.HeartAttackModel(age=int(decoded_content['age']),
                               sex=int(decoded_content['sex']), cp=int(decoded_content['cp']), trestbps=int(decoded_content['trestbps']), chol=int(decoded_content['chol']), fbs=int(decoded_content['fbs']), restecg=int(decoded_content["restecg"]), thalach=int(decoded_content["thalach"]), exang=int(decoded_content["exang"]), oldpeak=int(decoded_content["oldpeak"]), slope=int(decoded_content["slope"]), ca=int(decoded_content["ca"]), thal=int(decoded_content["thal"]))
        response_data = {}

        


        try:
            obj = util.Utility_()
            result = str(obj.get_heart_attack(
                request_obj=request, data=heart_object))[2:-1]
            decoded_result = ast.literal_eval(result)
        except:
            response_data['result'] = "error"
            response_data['status'] = 500
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        
        print(decoded_result)
        response_data['result'] = decoded_result['Result']
        response_data['status'] = decoded_result['Status']
    return HttpResponse(json.dumps(response_data), content_type="application/json")


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

        template = loader.get_template('pages/error-404.html')
        return HttpResponse(template.render(context, request))
