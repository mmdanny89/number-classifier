
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
import server_api


def prepare_data_to_classify(numbers):
    result = {'Number':[]}
    for x in range(len(numbers)):
        result['Number'].append(int(np.base_repr(numbers[x],base=3)))
    df = pd.DataFrame(result)
    return df


def classify_(numbers=None):
    df = pd.read_csv("./data_train/data.csv")
    X = df.drop('Type', axis=1)
    y = df['Type']
    for i in range(len(df)):
        X.at[i,'Number']= int(np.base_repr(int(X.at[i,'Number']), base=3))
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    #clf = LinearSVC()
    #clf = GaussianNB()
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    result = None 
    if numbers:
        result = clf.predict(prepare_data_to_classify(numbers))
        acc = None
    else:
        result = clf.predict(X_test)
        acc = (accuracy_score(y_test, result)*100)
    return result, acc


if __name__ == '__main__':
    result, acc = classify_([90,100,1,45])
    msg = "****Accuarcy: {0}".format(str(acc))
    print(msg)
    server_api.run_server(str(result))
    