import pandas as pd
import numpy as np
import sklearn.preprocessing 
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import mutual_info_classif

dataset = pd.read_csv('maline_fvt2.csv')

#print(dataset.head)


X = dataset.iloc[:, 1:105].values
y = dataset.iloc[:,0].values

#print(X)


##normalize


scaler = MinMaxScaler()
scaler.fit(X)
MinMaxScaler(copy=True, feature_range=(0, 1))

X_normalized = scaler.transform(X)

print(X_normalized.shape)





##feature selection(mutual info)

scores=mutual_info_classif(X_normalized,y)

print(scores)

np.savetxt("mutual_info_hello.csv",scores, delimiter=",")


'''
##################################
from skfeature.function.statistical_based import gini_index

score = gini_index.gini_index(X, y)

print(score)
np.savetxt("gini_index2.csv",score, delimiter=",")



score = gini_index.gini_index(X_normalized, y)

print(score)


'''
#sel.transform(X)


#print(sel.scores_)

#np.savetxt("deb.csv", sel.scores_, delimiter=",")

'''

####creating the table

l=list(dataset.columns.values)

l=l[1:157]
score=sel.scores_
df = pd.DataFrame({'system_call': pd.Series(l, dtype=str), 'chi_score': pd.Series(score, dtype=float)})
columnsTitles=['system_call','chi_score']
df=df.reindex(columns=columnsTitles)

df['Feature_Rank'] = df['chi_score'].rank(ascending=False)
df=df.sort_values(by=['Feature_Rank'])
df.to_csv("score4.csv",index=False)


#print(sel.scores_)
#np.savetxt("foo.csv", sel.scores_, delimiter=",")

'''
