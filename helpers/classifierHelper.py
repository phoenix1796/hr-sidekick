from sklearn.externals import joblib
import pickle

#External Libs
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report

#External Algos
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def _loadClassifier(filename):
    return joblib.load(filename)

def predict(input,classifierName):
    clf = _loadClassifier("classifiers/%s.pkl" % classifierName)
    input = _preprocess([input]) # StandardScaler expects an Array of Arrays (2d array) ,
    return clf.predict(input)

#Required Inputs : satisfaction_level, <Scaled>
#                   last_evaluation, <Scaled>
#                   number_project, <Same as before>
#                   average_montly_hours, <Same as before>
#                   time_spend_company, <Same as before>
#                   Work_accident, <Boolean> 0/1
#                   promotion_last_5years, <Boolean> 0/1
#                   salary {
#                           high = 0
#                           low = 1
#                           medium = 2
#                           }
#Sample Row:
#satisfaction_level 	last_evaluation 	number_project 	average_montly_hours 	time_spend_company 	Work_accident 	promotion_last_5years 	salary
# 0.38 	                0.53 	            2 	            157 	                    3 	                0 	            0 	                    1
def _preprocess(input, classifierPath = "classifiers/standardScaler.pkl"):
    with open(classifierPath,'rb') as f:
        standardScaler = pickle.loads(f.read())
    return standardScaler.transform(input)

if __name__=="__main__":
    # print(_preprocess([[0.38,0.53,2,157,3,0,0,1]])) # Only for my use
    #To predict for any data just import the predict function and call as done below .
    print(predict([0.38,0.53,2,157,3,0,0,1],"randomForest"))