import pandas as pd
import numpy as np
import scipy.stats

dataset = pd.read_csv('small_dataset.csv')


#####creating the contingency table

n=len(dataset.columns)

X=dataset.iloc[:,1:n].values

l=len(X)


pscore = []

for i in range(n-1):
    
    X_column=X[:,i]
    neg_array,pos_array=np.hsplit(X_column,2)
    #print(pos_array.size)
    a=np.count_nonzero(pos_array)
    b=np.count_nonzero(neg_array)
    c= l/2-a
    d= l/2-b
    temp_score = 0
    contingency_table=np.array([[a,b],[c,d]])
    temp_score= scipy.stats.chi2_contingency(contingency_table,correction=False)[1]
    pscore.append(temp_score)
    '''
    if temp_score < 0.05:
        pscore.append(0)
    else:       
        pscore.append(temp_score)
    '''
    
    
np.savetxt("pscore_chi.csv",pscore, delimiter=",") 
    
    
    
    
    
    
    
    
    


