# Today we will explore a data set dedicated to the cost of treatment of different patients.
# The cost of treatment depends on many factors: diagnosis, type of clinic, city of residence,
# age and so on. We have no data on the diagnosis of patients. But we have other information 
# that can help us to make a conclusion about the health of patients and practice regression analysis.
#  In any case, I wish you to be healthy! Let's look at our data.

import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as pl
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.ensemble import RandomForestRegressor

#Reading the data from the file 
# data = pd.read_csv('../input/insurance.csv')
data = pd.DataFrame()
x_train = pd.DataFrame()
y_tranin = pd.DataFrame()
x_test = pd.DataFrame()
y_test = pd.DataFrame()
class Training_module:

    def read_data(self):
        self.data = pd.read_csv('C:\\Users\\yatin.arora\\Desktop\\insurance cost\\insurance.csv')
        print(self.data.head())
        print("Data readed successfully")
        return self.data

    def preprocessing(self):
        print("preprocessing for data")
        le = LabelEncoder()
        le.fit(self.data.sex.drop_duplicates()) 
        self.data.sex = le.transform(self.data.sex)
        # smoker or not
        le.fit(self.data.smoker.drop_duplicates()) 
        self.data.smoker = le.transform(self.data.smoker)
        #region
        le.fit(self.data.region.drop_duplicates()) 
        self.data.region = le.transform(self.data.region)

    def view_data(self):
        print("viewing data")
        print(self.data.head(5))

    def visualizing(self):
        print("Visulaization")

        print("Checking Data which is NIL")
        print(self.data.isnull().sum())
        self.data.boxplot(column="charges",by="region", figsize=(18, 8))
        
        #checking smokers count based in gender 
        sns.catplot(x="smoker", kind="count",hue = 'sex', palette="pink", data=data)




    def correlation(self):
        f, ax = pl.subplots(figsize=(10, 8))
        corr = self.data.corr()
        sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(240,10,as_cmap=True),
            square=True, ax=ax)
    
    def modeling(self,model):
        x = self.data.drop(['charges'], axis = 1).values
        y = self.data['charges'].values
        self.x_train,self.x_test,self.y_train,self.y_test = train_test_split(x,y, random_state = 42)
        lr = LinearRegression().fit(self.x_train,self.y_train)
        return lr



model_obj = Training_module()
df_data = model_obj.read_data()
model_obj.preprocessing()
model_obj.view_data()
# model_obj.visualizing()
#Hence proved no data is null

model_obj.correlation()
#So from above correlation we can see that we are having strong correlation between charges and the smoking habbit


from sklearn.linear_model import LinearRegression

clf = model_obj.modeling(model = LinearRegression())

#save model using pickle 
import pickle
filename = 'C:\\Users\\yatin.arora\\Desktop\\insurance cost\\linear_regression.sav'
pickle.dump(clf, open(filename, 'wb'))





