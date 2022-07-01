
from sklearn import svm
from sklearn.svm import SVC
from sklearn import datasets

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics

import numpy as np
from sklearn.preprocessing import StandardScaler, Binarizer, MinMaxScaler, normalize
from sklearn import preprocessing
from sklearn.preprocessing import OrdinalEncoder

import pandas as pd


def classify():
    #X, y = datasets.make_blobs(n_samples=100, center_box=(1,100), centers=4)
    #X_train, X_test, y_train, y_test = train_test_split(X, y)
    #print(X_train)
    #svclassifier = SVC(C=100)
    #svclassifier.fit(X_train, y_train)
    #y_p = svclassifier.predict(X_test)
    #print(y_p)
    #none_m = [1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49, 52, 53, 56, 58, 59, 61, 62, 64, 67, 68, 71, 73, 74, 76, 77, 79, 82, 83, 86, 88, 89, 91, 92, 94, 97, 98]
    #fizz = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #buzz = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    #fizz_buzz = [15, 30, 45, 60, 75, 90]

    #iris = datasets.load_iris()
    #X = [fizz_buzz, buzz]#iris.data
    #y = ['fizz_buzz', 'buzz']#iris.target
    #X_train, X_test, y_train, y_test = train_test_split(X, y)
    #print("Xtrain: ",X_train, "Xtest: ",X_test, "y_train: ",y_train, "y_test: ",y_test)
    
    
    df = pd.read_csv("/home/danny/model.csv")
    
    encoder = OrdinalEncoder(categories=['None', 'Fizz', 'Buzz', 'FizzBuzz'])
    cat = pd.Categorical(df.Type, categories=['None', 'Fizz', 'Buzz', 'FizzBuzz'], ordered=True)
    labels, unique = pd.factorize(cat, sort=True)
    df.Type = labels
    scaler = StandardScaler()
    t = scaler.fit_transform(df.Number.values.reshape(-1, 1))
    df.Number = t
    #print(df.values)
    df_norm = normalize(df.values, "l2", axis=1)
    
    
    #X = df.drop('Type', axis=1)
    #y = df['Type']
    #print(df['Type'].value_counts())
    #print(df.info())
    #print(round(df.describe(),2))
    
    #print(X)

    #X_digits, y_digits = datasets.load_digits(return_X_y=True)

    #X = scaler.transform(X)
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    

    #print(X_train.append([2]))
    #print(X_test.shape)
    

    #print(X_train.describe())


    
    #svclassifier = SVC(C=100)
    #svclassifier.fit(X_train, y_train)
    #predict = svclassifier.predict(X_test)
    #print(predict)
    
    #print('Model accuracy score with rbf kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

    
    #y_pred = svclassifier.predict([[69],[70], [71]])
    #print(y_pred)
    #print(y_pred)
    #accuracy = accuracy_score(y_test,y_pred)*100
    #print(accuracy)
    #print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred,zero_division=1))

    #X_train, X_test, y_train, y_test = train_test_split(X, y)

       

    #SupportVectorClassModel = svm.SVC(kernel='linear')
    #SupportVectorClassModel.fit(X_train, y_train)

    #y_pred = SupportVectorClassModel.predict([[7],[100]])


    #accuracy = accuracy_score(y_test,y_pred)*100
    #print("y_pred: ", y_pred)
    #print("accuracy: ", accuracy)


def separate_numbers():
    none_m = []
    fizz = []
    buzz = []
    fizz_buzz = []
    for i in range(1,101):
        if i % 3 == 0:
            fizz.append(i)
        if i % 5 == 0:
            buzz.append(i)
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz.append(i)
        elif not i % 3 == 0 and not i % 5 == 0:
            none_m.append(i)

    print('----none----')
    print(none_m)
    print('----fizz----')
    for i in range(len(none_m)-len(fizz)):
        pass
    print(fizz)
    print('----buzz----')
    print(buzz)
    print('----fizz_buzz----')
    print(fizz_buzz)



if __name__ == '__main__':
    classify()
