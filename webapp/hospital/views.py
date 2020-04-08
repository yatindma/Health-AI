from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import requests
from .forms import StaffSchedule_form
from predictions import utility  as util
import json
import ast


@login_required(login_url="/login/")
def index(request):

    return render(request, "hospitalindex.html")

@login_required(login_url="/login/")
def StaffSchedule(request):
    
    form = StaffSchedule_form(request.POST or None)

    if request.method == "POST":   # return render(request,"prediction.html")
        content = request.body
        # Converting byte to string using content.decode
        json_content = content.decode('ASCII')
        decoded_content = json.loads(json_content)

        print(decoded_content)











        if form.is_valid():
            
            # return HttpResponse("insurance predictor is running")
            #We'll predict heart attack -->  from flask and return using context
            FromDate = form.cleaned_data["FromDate"]            
            ToDate = form.cleaned_data["ToDate"]
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(FromDate)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            dict = {}
            dict['FromDate'] = request.POST["FromDate"]
            dict['ToDate'] = request.POST["ToDate"]

           

            return render(request, "hospitalindex.html")
        return HttpResponse("form is not reaching")
    return HttpResponse("form is not valid")