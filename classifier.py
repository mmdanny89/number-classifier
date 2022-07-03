
from pg8000 import Binary
from sklearn import svm
from sklearn.svm import SVC, LinearSVC
from sklearn import datasets

import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
import numpy as np
from sklearn.preprocessing import StandardScaler, Binarizer, MinMaxScaler, normalize
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder, QuantileTransformer

from sklearn import random_projection

import pandas as pd

import server_api


def prepare_data_to_classify(numbers):
    result = {'Number':[]}
    for x in range(len(numbers)):
        result['Number'].append(int(np.base_repr(numbers[x],base=3)))
    df = pd.DataFrame(result)
    return df


def classify_linear_svc(numbers=None):
    cwd = os.getcwd()
    df = pd.read_csv(f"{cwd}/data_train/data.csv")
    X = df.drop('Type', axis=1)
    y = df['Type']
    for i in range(len(df)):
        X.at[i,'Number']= int(np.base_repr(int(X.at[i,'Number']), base=3))
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    linear_svc = LinearSVC()
    linear_svc.fit(X_train, y_train)
    result = None 
    if numbers:
        result = linear_svc.predict(prepare_data_to_classify(numbers))
        acc = None
    else:
        result = linear_svc.predict(X_test)
        acc = (accuracy_score(y_test, result)*100)
    return result, acc


if __name__ == '__main__':
    result, acc = classify_linear_svc([90,100,1,45])
    print(acc)
    server_api.run_server(str(result))
    