#utility class
# import flask
import requests
from django.forms.models import model_to_dict
import json
from django.core import serializers
class Utility_:
    
    def get_heart_attack(self,request_obj,data):
        # post_list = serializers.serialize('json', data)
        # heart_conv_obj = model_to_dict(data)
        # xx = json.dumps(data)
        content = {}
        content['age'] = data.age
        content['sex'] = data.sex
        content['cp'] = data.cp
        content['fbs'] = data.fbs
        content['exang'] = data.exang
        content['trestbps'] = data.trestbps
        content['chol'] = data.chol
        content['restecg'] = data.restecg
        content['thalach'] = data.thalach
        content['oldpeak'] = data.oldpeak
        content['slope'] = data.slope
        content['ca'] = data.ca
        content['thal'] = data.thal
        
        

        url = "http://127.0.0.1:5000/predict/"
        payload = json.dumps(content)
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data = payload)

        return response.text.encode('utf8')
        # return "hello bro"

    def check_services(self,request_obj):
        response = requests.get('http://127.0.0.1:5000/')


