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
    return "Service Running"

@app.route('/predict/',methods= ['POST'])
def predictor():

    try:
        
        req_data = request.get_json()

        InputData = np.array([req_data['age']])
        InputData = np.append(InputData,[req_data['sex']])
        InputData = np.append(InputData,[req_data['cp']])
        InputData = np.append(InputData,[req_data['trestbps']])
        InputData = np.append(InputData,[req_data['chol']])
        InputData = np.append(InputData,[req_data['fbs']])
        InputData = np.append(InputData,[req_data['restecg']])
        InputData = np.append(InputData,[req_data['thalach']])
        InputData = np.append(InputData,[req_data['exang']])
        InputData = np.append(InputData,[req_data['oldpeak']])
        InputData = np.append(InputData,[req_data['slope']])
        InputData = np.append(InputData,[req_data['ca']])
        InputData = np.append(InputData,[req_data['thal']])

        from sklearn.ensemble import RandomForestClassifier
        filename = 'C:\\Users\\yatin.arora\\Desktop\\heati_health\\model.sav'
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


@app.route('/accuracy/')
def accuracy():
    try:
        from sklearn.ensemble import RandomForestClassifier
        filename = 'C:\\Users\\yatin.arora\\Desktop\\heati_health\\model.sav'
        clf = pickle.load(open(filename, 'rb'))
        # clf.crossValScore(cv=10)
        # accuarcy = accuracy_score(no_data, y_no_data)
        # Reading the data from the CSV file
        df = pd.read_csv("C:\\Users\\yatin.arora\\Desktop\\Case Study\\HeartiHealth\\ML Hearti Health\\heart.csv")

        # Define our features and labels
        X = df.drop(['target'], axis=1).values
        y = df['target'].values
        print("reached 1")


      
        # return bytes_image
        plt.figure(figsize=(5, 5))
        mat = confusion_matrix(y, y)
        sns.heatmap(mat.T, square=True, 
                    annot=True, 
                    cbar=False, 
                    xticklabels=["Haven't Disease", "Have Disease"], 
                    yticklabels=["Haven't Disease", "Have Disease"])
        
        # plt.title(self.model_str() + " Confusion Matrix")
        plt.xlabel('Predicted Values')
        plt.ylabel('True Values');
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        print("reached 2")
        # return 
        print(type(send_file(bytes_image,
                     attachment_filename='plot.png',
                     mimetype='image/png')))

        # dict = {}
        # dict['Result'] = send_file(bytes_image,
        #              attachment_filename='plot.png',
        #              mimetype='image/png')
        # dict['Status'] = 200
        return send_file(bytes_image,
                     attachment_filename='plot.png',
                     mimetype='image/png')
        
    except Exception as e:
        
        dict = {}
        dict['Result'] = "Something went wrong..!! " + str(e)
        dict['Status'] = 500     
        return dict  