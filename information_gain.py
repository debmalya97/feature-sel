import pandas as pd
import numpy as np
import scipy.stats
from math import log

'''

http://nmis.isti.cnr.it/sebastiani/Publications/ACMCS02.pdf

'''

dataset = pd.read_csv('maline_fvt2.csv')


#####creating the contingency table

n=len(dataset.columns)  #no of columns

X=dataset.iloc[:,1:n].values

l=len(X) #no or rows


score = []

for i in range(n-1):
    #print(i)
    
    X_column=X[:,i]
    neg_array,pos_array=np.hsplit(X_column,2)
    #print(pos_array.size)
    a=np.count_nonzero(pos_array)
    b=np.count_nonzero(neg_array)
    c= l/2-a
    d= l/2-b
    M=a+b
    tmp=0
    #temp_score=a*l
    #score.append(temp_score)
    list = [a,b,c,d]
    print(a,b,c,d)
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    
    '''
    for i in list:
    
        if i==0:
            tmp= 0
            
        else:
            tmp += i*log((i/(M*n)))
            
     '''
    if a==0:
     
        tmp1 = 0
    else :
        tmp1= a*log(a/((a+b)*(a+c)))
        
    if b==0:
     
        tmp2 = 0
    else :
        tmp2= b*log(b/((a+b)*(b+d))) 

    if c==0:
     
        tmp3 = 0
    else :
        tmp3= c*log(c/((c+d)*(a+c)))

    if d==0:
     
        tmp4 = 0
    else :
    
        tmp4= d*log(d/((c+d)*(b+d)))        
        

      
    tmp = tmp1 + tmp2 + tmp3 + tmp4
    #print(((a*l)/((a+c)*(a+b))))
    
    
    score.append(tmp)
    
    '''
    if temp_score < 0.05:
        pscore.append(0)
    else:       
        pscore.append(temp_score)
    '''
    
    
np.savetxt("information_gain.csv",score, delimiter=",") 
    

    
    
    
    
    
    
    


