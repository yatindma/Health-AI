
# Machine Learning Model Libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import XGBClassifier

#Enumeration
from enum import Enum


class ModelFactory:
    """
        Creating factory class to get object of the models.
    """

    def factory(model_name):
        """
            initialising & returning model
        """

        model = ()
        if model_name == Models.randomForest: 
            model = RandomForestClassifier()
            
        elif model_name == Models.Xgb: 
            model = XGBClassifier()
        
        #######################################
                #ADD MORE MODELS HERE --> KNN KD Tree/Naive Bayes/Logistic Regression/SVM/Decision Tree/Catboost
        #######################################

        return model

    factory = staticmethod(factory)


class Models(Enum):
    """
        add new model name here.
    """
    randomForest = 'RandomForest'
    xgb = 'XGB'