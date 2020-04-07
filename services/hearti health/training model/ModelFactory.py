
from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import XGBClassifier


class ModelFactory:
    def factory(model_name):
        if model_name == "RandomForest": return RandomForestClassifier()
        elif model_name == "XGB": return XGBClassifier()

    factory = staticmethod(factory)



#     def create(modelname):
#         model = null;
#         if(modelname=Models.model1):
#             model=RandomForestClassifier()
#         elif (modelname=Models.model2):
#             model=XGBClassifier()
#         return model

 

# class Models(enum.Enum):
#    model1 = 'RandomForest'
#    model2 = 'XGB'