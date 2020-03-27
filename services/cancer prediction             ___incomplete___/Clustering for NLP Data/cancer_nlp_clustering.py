import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import warnings
warnings.simplefilter("ignore")

#Reading data 
data = pd.DataFrame()   #so there are 5 text fields which are missing.

#Set of stop words . here we removed words like not ,nor
stop_words= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])

X_train = pd.DataFrame()
y_train = pd.DataFrame()
X_test = pd.DataFrame()
y_test = pd.DataFrame()
X_cv = pd.DataFrame()
y_cv = pd.DataFrame()

class DataPreProcess:
    def reading_data(self):
        self.data = pd.read_excel('C:\\Users\\yatin.arora\\Desktop\\Clustering_heart_predictor\\randomized.xlsx')
        print(self.data.head(2))
        print(self.data.isnull().sum())
        


    def data_processing(self):
        #Updating the text which are nil with 'text' + 'variation'
        self.data.loc[self.data['TEXT'].isnull(),'TEXT'] = self.data['Gene'] +' '+self.data['Variation']
        print("Reached to data+ process")
        data_text = []
        count = 0
        for index,text in enumerate(self.data.TEXT.values):
            string = ""
            if type(text) is not int:
                # replace every special char with space
                text = re.sub('[^a-zA-Z0-9\n]', ' ', text)
                # converting all the chars into lower-case.
                text = text.lower()
                for word in text.split():
                # if the word is a not a stop word then retain that word from the data
                    if not word in stop_words:
                        string += word + " "
            data_text.append(string)
        
        self.data['TEXT'] = data_text
        self.data.Gene      = self.data.Gene.str.replace('\s+', '_')
        self.data.Variation = self.data.Variation.str.replace('\s+', '_')
        

    def train_test_splitting(self):
        
        y_true = self.data['Class']
        X = self.data
        # split the data into test and train by maintaining same distribution of output varaible 'y_true' [stratify=y_true]
        X_train_temp, self.X_test, y_train_temp, self.y_test = train_test_split(X, y_true, stratify=y_true, test_size=0.2)
        # split the train data into train and cross validation by maintaining same distribution of output varaible 'y_train' [stratify=y_train]
        self.X_train, self.X_cv, self.y_train, self.y_cv = train_test_split(X_train_temp, y_train_temp, stratify=y_train, test_size=0.2)
    
    def distiribution_of_class(self):
        self.data['Class'].value_counts().plot(kind="bar", rot=0)
        print("here at distribution")
        plt.show()

        




class Model:
    
    list_ = list(data.columns.array)
    print(list_)
    test_data_len = X_test.shape[0]
    cv_data_len = X_cv.shape[0]
    train_data_len = X_train.shape[0]

    # ref: https://stackoverflow.com/a/18662466/4084039
    def randomized_model(self):
        print("random")
        # we create a output array that has exactly same size as the CV data
        cv_predicted_y = np.zeros((self.cv_data_len,9))
        for i in range(self.cv_data_len):
            rand_probs = np.random.rand(1,9)
            cv_predicted_y[i] = ((rand_probs/sum(sum(rand_probs)))[0])


        #same as previous again we'll create random array for test data
        test_predicted_y = np.zeros((self.test_data_len,9))
        for i in range(self.test_data_len):
            rand_probs = np.random.rand(1,9)
            test_predicted_y[i] = ((rand_probs/sum(sum(rand_probs)))[0])


        #we'll check for train data

        train_predicted_y = np.zeros((self.train_data_len,9))
        for i in range(self.train_data_len):
            rand_probs = np.random.rand(1,9)
            train_predicted_y[i] = ((rand_probs/sum(sum(rand_probs)))[0])

    def confusionMatrix(self,y_orig,y_pred,label):        
        plt.figure(figsize=(20,7))
        mat = confusion_matrix(y_orig, y_pred)
        sns.heatmap(mat, annot=True, cmap="YlGnBu", fmt=".3f", xticklabels=label, yticklabels=labels)
        plt.xlabel('Predicted Values')
        plt.ylabel('True Values');
        plt.show();
        return mat        

    def precision_matrix(self,matrix,labels):
        labels = [1,2,3,4,5,6,7,8,9]
        plt.figure(figsize=(20,7))
        sns.heatmap(matrix, annot=True, cmap="YlGnBu", fmt=".3f", xticklabels=labels, yticklabels=labels)




labels = [1,2,3,4,5,6,7,8,9]
process_obj = DataPreProcess()
process_obj.reading_data()
process_obj.data_processing()
process_obj.train_test_splitting()
# process_obj.distiribution_of_class(self.X_train)
# process_obj.distiribution_of_class(self.X_test)
# process_obj.distiribution_of_class(self.X_cv)

modeling = Model()
modeling.randomized_model()
cf_m = modeling.confusionMatrix(y_orig = y_cv ,y_pred= y_cv,label=labels)
recall_matrix =(((cf_m.T)/(cf_m.sum(axis=1))).T)
precision_matrix = (cf_m/cf_m.sum(axis=0))
precision_matrix(matrix=precision_matrix,labels = labels)
precision_matrix(matrix=recall_matrix,labels = labels)





# cv_predicted_y
# predicted_y =np.argmax(cv_predicted_y, axis=1)
# print("*"*50)
# print("confusion matrix on CV data")
# cf_m = confusionMatrix(y_cv,predicted_y)
# recall_matrix =(((cf_m.T)/(cf_m.sum(axis=1))).T)
# precision_matrix = (cf_m/cf_m.sum(axis=0))

