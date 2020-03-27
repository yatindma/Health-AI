import numpy as np
from flask import Flask,request,Response,send_file
import pandas as pd
import pickle
import json
from sklearn.metrics import accuracy_score,confusion_matrix
import io
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")
app = Flask(__name__)



@app.route('/')
def index():
    return "insurance Service Running"


@app.route('/ipredict/',methods= ['POST'])
def predictor():

    try:
        req_data = request.get_json()

        InputData = np.array([req_data['age']])
        InputData = np.append(InputData,[req_data['sex']])
        InputData = np.append(InputData,[req_data['bmi']])
        InputData = np.append(InputData,[req_data['children']])
        InputData = np.append(InputData,[req_data['smoker']])
        InputData = np.append(InputData,[req_data['region']])

        from sklearn.ensemble import RandomForestClassifier
        filename = 'C:\\Users\\yatin.arora\\Desktop\\insurance cost\\linear_regression.sav'
        clf = pickle.load(open(filename, 'rb'))
        # clf.crossValScore(cv=10)
        # clf.accuracy()
        df = np.array(InputData).reshape(1,-1)
        result = clf.predict(df)

        dict = {}
        dict['Result'] = result[0]
        dict['Status'] = 200

    except KeyError as e:
        
        dict = {}
        dict['Result'] = "Key missing " + str(e)
        dict['Status'] = 500

    except Exception as e:
        
        dict = {}
        dict['Result'] = "Something went wrong..!! " + str(e)
        dict['Status'] = 500

    response = str(dict)
    return response
