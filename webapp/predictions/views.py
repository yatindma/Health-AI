from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import requests
from .forms import attack_prediction_form
from predictions import utility  as util
import json
import ast
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
        if form.is_valid():
            # return HttpResponse("insurance predictor is running")
            #We'll predict heart attack -->  from flask and return using context
            age = form.cleaned_data["age"]            
            sex = form.cleaned_data["sex"]
            cp = form.cleaned_data["cp"]           
            trestbps = form.cleaned_data["trestbps"]
            chol = form.cleaned_data["chol"]
            fbs = form.cleaned_data["fbs"]
            restecg = form.cleaned_data["restecg"]
            thalach = form.cleaned_data["thalach"]
            exang = form.cleaned_data["exang"]
            oldpeak = form.cleaned_data["oldpeak"]
            slope = form.cleaned_data["slope"]
            ca = form.cleaned_data["ca"]
            thal = form.cleaned_data["thal"]

            dict = {}
            dict['age'] = age
            dict['sex'] = sex
            dict['cp'] = cp
            dict['trestbps'] = trestbps
            dict['chol'] = chol
            dict['fbs'] = fbs
            dict['restecg'] = restecg
            dict['thalach'] = thalach
            dict['exang'] = exang
            dict['oldpeak'] = oldpeak          
            dict['slope'] = slope
            dict['ca'] = ca             
            dict['thal'] = thal  
            print("jjjjjjjjjjjjjjjjjjj")
            print(dict)
            print("jjjjjjjjjjjjjjjjjjj")
            obj = util.Utility_()
            result = str(obj.get_heart_attack(request_obj = request,json_data = json.dumps(dict) ))[1:]
            y = ast.literal_eval(result)
            data = []
            data.append(str(y[1]))
            context = {'response': result}
            return render(request,"prediction_from_heart_attack.html",context=context)
        return HttpResponse("form is not reaching")
    return HttpResponse("form is not valid")
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

	