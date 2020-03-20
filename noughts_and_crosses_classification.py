#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import sys
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier

le = preprocessing.LabelEncoder()

def Tic_Tac_Toe(method):
    
    # Read in data
    data = pd.read_csv('tic-tac-toe.data', sep=',')
        
    # Convert data from Xs and Os to numbers
    arr1 = LabelEncoder().fit_transform(data['1'])
    arr2 = LabelEncoder().fit_transform(data['2'])
    arr3 = LabelEncoder().fit_transform(data['3'])
    arr4 = LabelEncoder().fit_transform(data['4'])
    arr5 = LabelEncoder().fit_transform(data['5'])
    arr6 = LabelEncoder().fit_transform(data['6'])
    arr7 = LabelEncoder().fit_transform(data['7'])
    arr8 = LabelEncoder().fit_transform(data['8'])
    arr9 = LabelEncoder().fit_transform(data['9'])
    arr_res = LabelEncoder().fit_transform(data['result'])
        
    data['1'] = arr1
    data['2'] = arr2
    data['3'] = arr3
    data['4'] = arr4
    data['5'] = arr5
    data['6'] = arr6
    data['7'] = arr7
    data['8'] = arr8
    data['9'] = arr9
    data['result'] = arr_res
            
    # X is the input configuration of Xs and Os, y is the result (positive is a win for X)
    X = data.drop('result', axis=1)
    y = data['result']
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Fit to training set and predict
    if (method == 'linSVC'):
        clf = LinearSVC(random_state=0, tol=1e-5)
        clf.fit(X_train, y_train)
        y_predict = clf.predict(X_test)
    elif(method == 'kneigh'):
        neigh = KNeighborsClassifier(n_neighbors=3)
        neigh.fit(X_train, y_train)
        y_predict = neigh.predict(X_test)
    elif (method == 'SVC'):
        clf = SVC(gamma='auto')
        clf.fit(X_train, y_train)
        y_predict = clf.predict(X_test)
    elif (method == 'Bag'):
        clf = BaggingClassifier(base_estimator=SVC(),n_estimators=10, random_state=0).fit(X_train, y_train)
        y_predict = clf.predict(X_test)
    else:
        print('method {0} not available for input'.format(method))
        sys.exit(0)
            
    # Calculate accuracy of prediction, using ratio of correct predictions to number of predictions
    correct = len(y_predict[y_predict == y_test])
    accuracy = correct/len(y_predict)
    
    return accuracy






if __name__ == '__main__':
    print('The accuracy ratio is the ratio of correct predictions to the number of predictions')
    
    Accuracy_Ratio_lin_SVC = Tic_Tac_Toe('linSVC')
    print('The accuracy ratio using LinearSVC is {0}'.format(Accuracy_Ratio_lin_SVC))
    
    Accuracy_Ratio_KN = Tic_Tac_Toe('kneigh')
    print('The accuracy ratio using KNearest Neighbours is {0}'.format(Accuracy_Ratio_KN))
    
    Accuracy_Ratio_SVC = Tic_Tac_Toe('SVC')
    print('The accuracy ratio using SVC is {0}'.format(Accuracy_Ratio_SVC))
    
    Accuracy_Ratio_Bag = Tic_Tac_Toe('Bag')
    print('The accuracy ratio using BaggingClassifier is {0}'.format(Accuracy_Ratio_Bag))
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    