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



# @Login_required is added to readch to login page if some one tries to log in
@login_required(login_url="/login/")
def heart_attack_prediction(request):
    """
        Redirecting html page "heart_predict.html" 
    """
    return render(request, "heart_predict.html")


@login_required(login_url="/login/")
def heart_attack_report(request):

    """
        Calling prediction server and sending data as an Object to the prediction server,
            getting the response as string in json format
                and returning back the response using HttpResponse
    """
    response_data = {}
    if request.method == "POST":
        content = request.body
        # Converting byte to string using content.decode
        json_content = content.decode('ASCII')
        decoded_content = json.loads(json_content)
        

        # Creating object after fetching value from the json request
        heart_object = models.HeartAttackModel(age=int(decoded_content['age']),
                               sex=int(decoded_content['sex']), cp=int(decoded_content['cp']), trestbps=int(decoded_content['trestbps']), chol=int(decoded_content['chol']), fbs=int(decoded_content['fbs']), restecg=int(decoded_content["restecg"]), thalach=int(decoded_content["thalach"]), exang=int(decoded_content["exang"]), oldpeak=int(decoded_content["oldpeak"]), slope=int(decoded_content["slope"]), ca=int(decoded_content["ca"]), thal=int(decoded_content["thal"]))
        #Calling server to predict
        try:
            obj = util.Utility_()
            result = str(obj.get_heart_attack(
                request_obj=request, data=heart_object))[2:-1]

            # Converting String to JSON
            decoded_result = ast.literal_eval(result)


            response_data['result'] = decoded_result['Result']
            response_data['important_features'] =  decoded_result['important_features'] 
            response_data['imp_features_weight'] = decoded_result['imp_features_weight']
            response_data['status'] = decoded_result['Status']            
        except:
            response_data['result'] = "error"
            response_data['status'] = 500            

    return HttpResponse(json.dumps(response_data), content_type="application/json")

