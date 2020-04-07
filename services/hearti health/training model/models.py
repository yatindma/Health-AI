
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import XGBClassifier


class ModelFactory:
    def factory(model_name):
        if model_name == Models.model1: return RandomForestClassifier()
        elif model_name == Models.model2: return XGBClassifier()

    factory = staticmethod(factory)


 

class Models(enum.Enum):
   model1 = 'RandomForest'
   model2 = 'XGB'