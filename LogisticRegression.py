import numpy as np

def sigmoid(x,div = False):
    if div==True:
        return x*(1-x)
    return 1/(1+np.exp(-x))
v = np.loadtxt("ex_data.txt",delimiter = ',')
# print(v[:,10]) # Slice examples
X = v[:,0:6]
y = v[:,10]
# np.size(X,0) # np.size(X,1) Size examples
# swing = np.where(y==0)
# right = np.where(y==1)
X = np.column_stack((np.ones([np.size(X,0),1]),X))
print(X)