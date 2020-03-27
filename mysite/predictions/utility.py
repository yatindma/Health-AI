#utility class
# import flask
import requests


class Utility_:
    
    def hhh(self):
        return "yatin arora came here"
    def get_heart_attack(self,request_obj):

        url = "http://127.0.0.1:5000/predict/"
        payload = "{\n    \"age\": 23,\n    \"sex\": 1,\n    \"cp\": 2,\n    \"trestbps\": 122,\n    \"chol\": 150,\n    \"fbs\": 1,\n    \"restecg\": 0,\n    \"thalach\": 187,\n    \"exang\": 0,\n    \"oldpeak\": 2.3,\n    \"slope\": 0,\n    \"ca\": 0,\n    \"thal\": 1\n}"
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data = payload)

        return response.text.encode('utf8')
        # return "hello bro"

    def check_services(self,request_obj):
        response = requests.get('http://127.0.0.1:5000/')


