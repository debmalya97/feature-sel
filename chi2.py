from __future__ import print_function
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LassoCV
from sklearn.feature_selection import chi2
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix
from sklearn import model_selection
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import argparse
import os.path as osp
import scipy.sparse as sp
import numpy as np
import pickle
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import sklearn.feature_selection


dataset = pd.read_csv('small_dataset.csv')
print(dataset.shape)


X = dataset.iloc[:,1].values
y = dataset.iloc[:,0].values
X_d= X.reshape(-1,1)
y_d=y.reshape(-1,1)
count=0
print(y_d.shape)

'''
for i in X:
    if i!=0:
        count+=1
print(count)
print(X)        
print("\n")
print(y)
'''

np.savetxt("X.csv", X, delimiter=",")
np.savetxt("y.csv", y, delimiter=",")
print(sklearn.feature_selection.chi2(X_d, y))

'''
sel.fit_transform(X, y)




#sel.transform(X)


print(sel.scores_)
print("\n")
print(sel.pvalues_)


np.savetxt("chi2_scores.csv", sel.scores_, delimiter=",")

'''