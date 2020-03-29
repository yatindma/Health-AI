#To remove warnings from python terminal
import warnings
warnings.simplefilter("ignore")

# linear algebra
import numpy as np 

# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd 

# Plotting graphs
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# Saving data
import pickle

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import os

# Import tools
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, auc

# Reading the data from the CSV file
df = pd.read_csv("C:\\Users\\yatin.arora\\Desktop\\Case Study\\HeartiHealth\\ML Hearti Health\\heart.csv")

# Define our features and labels
X = df.drop(['target'], axis=1).values
y = df['target'].values

class Model:
    df = pd.DataFrame()
    y_pred = []

    #Parameterised Constructor ( intializing data and model)
    def __init__(self,model, X, y):
        self.X = X
        self.y = y 
        self.model = model

    #dividing the data in train and test 
    def train_test_split(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.5, random_state=42)
    
    #Training the model
    def fit_the_model(self):
        # self.model098 = model
        self.model.fit(self.X_train,self.y_train)
        print(self.model_str()," model got trained")

    #Predicting for test data 
    def predicting(self):
        self.y_pred = self.model.predict(self.X_test)

    #Saving the trained model in local
    def dump_model(self,path):
        pickle.dump(self.model, open(path, 'wb'))

    #getting name of the model
    def model_str(self):
        return str(self.model.__class__.__name__)
    
    #using multiple scoring matrix 
    def crossValScore(self, cv=5):
        print(self.model_str() + "\n" + "="*60)
        scores = ["accuracy", "precision", "recall", "roc_auc"]
        for score in scores:  
            cv_acc = cross_val_score(self.model, 
                                     self.X_train, 
                                     self.y_train, 
                                     cv=cv, 
                                     scoring=score).mean()
            
            print("Model " + score + " : " + "%.3f" % cv_acc)
     
    #Getting accuracty score for test data
    def accuracy(self):
        accuarcy = accuracy_score(self.y_test, self.y_pred)
        print(self.model_str() + " Model " + "Accuracy is: ")
        return accuarcy
    
    #Creating confusion matrix
    def confusionMatrix(self):        
        plt.figure(figsize=(5, 5))
        mat = confusion_matrix(self.y_test, self.y_pred)
        sns.heatmap(mat.T, square=True, 
                    annot=True, 
                    cbar=False, 
                    xticklabels=["Haven't Disease", "Have Disease"], 
                    yticklabels=["Haven't Disease", "Have Disease"])
        
        plt.title(self.model_str() + " Confusion Matrix")
        plt.xlabel('Predicted Values')
        plt.ylabel('True Values')
        plt.show()

    #checking multiple matrixes to get better clarity on model training
    def classificationReport(self):
        print(self.model_str() + " Classification Report" + "\n" + "="*60)
        print(classification_report(self.y_test, 
                                    self.y_pred, 
                                    target_names=['Non Disease', 'Disease']))
    
    #getting ROC AUC curve to get better status of model tarining
    def rocCurve(self):
        y_prob = self.model.predict_proba(self.X_test)[:,1]
        fpr, tpr, thr = roc_curve(self.y_test, y_prob)
        lw = 2
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, 
                 color='darkorange', 
                 lw=lw, 
                 label="Curve Area = %0.3f" % auc(fpr, tpr))
        plt.plot([0, 1], [0, 1], color='green', 
                 lw=lw, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(self.model_str() + ' Receiver Operating Characteristic Plot')
        plt.legend(loc="lower right")
        plt.show()


#Importing model 
from sklearn.ensemble import RandomForestClassifier

#initialzing the model and the data
clf = Model(model=RandomForestClassifier(),X=X,y=y)    
#Dividing the data into train and test split
clf.train_test_split()  
#training the model
clf.fit_the_model()
#predicting outputs from the model using test data
clf.predicting()
#Checking crossvalidation score and 
clf.crossValScore()
#Get the classification report 
clf.classificationReport()
#to get the roc_auc curve for the model
clf.rocCurve()

#If model is working good save it.
filename = 'C:\\Users\\yatin.arora\\Desktop\\heati_health\\model.sav' #location you want to save the file
clf.dump_model(path= filename)



