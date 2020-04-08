#utility class
# import flask
import requests
from django.forms.models import model_to_dict
import json
from django.core import serializers
class Utility_:
    """
        Calling Rest Services 
    """
    
    def get_heart_attack(self,request_obj,data):
        """
            Calling heart attack prediction service 
        """
        content = {}
        url = "http://127.0.0.1:5000/predict/"

        #Converting object to dictionary
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
        
        #Converting dictionary to JSON
        payload = json.dumps(content)
        
        headers = {
        'Content-Type': 'application/json'
        }

        #Sending data to the prediction server and getting response.
        response = requests.request("POST", url, headers=headers, data = payload)

        return response.text.encode('utf8')



