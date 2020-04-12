#To remove warnings from python terminal
import warnings
warnings.simplefilter("ignore")
import models

# linear algebra Library
import numpy as np 

# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd 

# Plotting graphs Libraries
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

from pathlib import Path
# Reading the data from the CSV file
import os, sys

############################################
# Change Pandas to Dask
############################################
df = pd.DataFrame()
X = pd.DataFrame()
y = pd.DataFrame()

class Model:
    """
        Training,Testing and saving multiple Machine Learning models.
    """

    y_pred = []
    def read_data(self,file_path):
        """
            Reading the data from the csv
        """
        file_path = r"{}".format(file_path)
        self.df = pd.read_csv(str(file_path))
        self.X = self.df.drop(['target'], axis=1).values
        self.y = self.df['target'].values

        ###################################################
            #Perform Normalization or Standarisation
        ###################################################

    
    def execution_path(self,filename):
        """
            Getting the file path
        """
        return os.path.join(os.path.dirname(sys._getframe(1).f_code.co_filename), filename)

    #Parameterised Constructor ( intializing data and model)
    def __init__(self,model):
        """
            Initializing the data and model
        """
        self.model = model


    def train_test_split(self):
        """
            Dividing the data into training and testing ( 20% test data and 80% training data )
        """
        #######################################
            # Split and Randomize w/o using train_test_split()
        #######################################
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
    

    def fit_the_model(self):
        """
            Training the model
        """
        self.model.fit(self.X_train,self.y_train)
        print(self.model_str()," model got trained")


    def predicting(self):
        """
            Predicting from the model
        """
        self.y_pred = self.model.predict(self.X_test)

    
    def dump_model(self,path):
        """
            Saving the trained model in local
        """
        #######################################
            # Change the code here to use different dumper Libraries.
        #######################################
        
        pickle.dump(self.model, open(path, 'wb'))

    
    def model_str(self):
        """
            getting name of the model
        """
        return str(self.model.__class__.__name__)
    
     
    def crossValScore(self, cv=5):
        """
         Checking performsnce 
        """
        print(self.model_str() + "\n" + "="*60)
        scores = ["accuracy", "precision", "recall", "roc_auc"]
        for score in scores:  
            cv_acc = cross_val_score(self.model, 
                                     self.X_train, 
                                     self.y_train, 
                                     cv=cv, 
                                     scoring=score).mean()
            
            print("Model " + score + " : " + "%.3f" % cv_acc)
     
    
    def accuracy(self):
        """
            Returning model accuracy on test data
        """
        accuarcy = accuracy_score(self.y_test, self.y_pred)
        print(self.model_str() + " Model " + "Accuracy is: ")
        return accuarcy
    

    
    def confusionMatrix(self):  
        """
            Generating Confusion Matrix
            (This is done to determine how model is performing on negative and positive data)
        """      
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

    
    def classificationReport(self):
        """
            Checking multiplication report over the model performance
        """
        print(self.model_str() + " Classification Report" + "\n" + "="*60)
        print(classification_report(self.y_test, 
                                    self.y_pred, 
                                    target_names=['Non Disease', 'Disease']))
    
    #getting ROC AUC curve to get better status of model tarining
    def rocCurve(self):
        """
            Getting ROC AUC curve to check model performance
        """
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


#Getting model object using Factory method
model_obj = models.ModelFactory.factory(models.Models.dt)
#initialzing the model and the data
clf = Model(model=model_obj)  
path = str(clf.execution_path(""))[0:-1]
path_csv  = path + "/heart.csv"
clf.read_data(file_path=path_csv)
#Dividing the data into train and test split
clf.train_test_split() 

###################################
    #Add hyper tuning here
##################################

#training the model
clf.fit_the_model()
#predicting outputs from the model using test data
clf.predicting()
#Checking crossvalidation score and 
clf.crossValScore()
#Get the classification report 
clf.classificationReport()
#Getting confusion matrix
clf.confusionMatrix()
#to get the roc_auc curve for the model
clf.rocCurve()

########################################
    # Check model performance using Precision and Recall Matrix
########################################    


#If model is working good save it.
dumping_path = str(path) + "/model.sav"
print(dumping_path)
clf.dump_model(path= dumping_path)



