
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,Response,send_file
import pandas as pd
import pickle
import json
import ast
from sklearn.metrics import accuracy_score,confusion_matrix
import io
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from sklearn.preprocessing import normalize
# from ./predictions import models
warnings.simplefilter("ignore")
app = Flask(__name__)


@app.route('/')
def index():
    return "Service Running"

@app.route('/predict/',methods= ['POST'])
def predictor():
    dict = {}

    try:
        # features = eval(json.dumps(request.json))
        # data  = np.array(list(features.values())).reshape(1, -1)
        data = str(json.dumps(request.json))
        req_data = json.loads(data)        
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
        filename = 'C:\\Users\\yatin.arora\\Documents\\GitHub\\Health_predictor_using_AI\\services\\hearti health\\training model\\model.sav'
        clf = pickle.load(open(filename, 'rb'))

        df = np.array(InputData).reshape(-1,1)
        
        result = clf.predict([InputData])
        
        ############################################
         #Get probability from the the model and change your threshhold accordingly
        ############################################
        

        scale = StandardScaler()
        data_std = scale.fit_transform(df)
        data = []
        for content in data_std:
            data.append(content[0])


        
        
        

        #Getting important feature from the model
        importances = clf.feature_importances_
        #Names of the features
        features_name = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldPeak","slope","ca","thal"]
       
        #Average features of humanbeing
        avg_of_feature = [52,0.5,1,115,160,0.5,0.5,140,0.5,0.9,1,6,3]
        #Normalize the average feature data here
        df = np.array([avg_of_feature]).reshape(-1,1)
        scale = StandardScaler()
        normalized_feature_temp = scale.fit_transform(df)
        normalized_feature = []
        for cont in normalized_feature_temp:
            normalized_feature.append(cont[0])

        


        avg_weighted_feaature = []
        for index in range(0,len(avg_of_feature)):
            avg_weighted_feaature.append((normalized_feature[index] * importances[index] * 1000))

        
        patient_weighted_feat = []
        for index in range(0,len(avg_of_feature)):
            patient_weighted_feat.append((data[index] * importances[index] * 1000))


        diff_avg_and_patient = []
        for index in range(0,len(avg_of_feature)):
            diff_avg_and_patient.append(patient_weighted_feat[index] - avg_weighted_feaature[index])
        
        imp = np.argsort(importances)[::-1][:5]

        imp_feature_name = []
        imp_feature_diff = []
        count = 0
        for index in imp:
            imp_feature_name.append(features_name[index])
            imp_feature_diff.append(diff_avg_and_patient[index])


        imp = np.argsort(importances)[::-1][:5]
        string_arr = []
        

        for index in imp:
            string_arr.append(features_name[index])
            

        dict = {}
        dict['Result'] = str(result[0])
        dict['important_features'] = str(imp_feature_name)
        dict['imp_features_weight'] = str(imp_feature_diff)  
        dict['Status'] = 200

    except KeyError as e:
        
        dict = {}
        dict['Result'] = "Key missing " + str(e)
        dict['Status'] = 500

    except Exception as e:
        
        dict = {}
        dict['Result'] = "Something went wrong..!! " + str(e)
        dict['Status'] = 500

    
    
    response = str(json.dumps(dict))
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