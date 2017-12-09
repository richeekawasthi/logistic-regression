import math
import numpy as np
def sigmoid(m):
	return 1.0/(1.0+math.exp(-m))
def hypothesis(features,theta):
	return sigmoid(np.dot(features,np.transpose(theta)))

theta=np.load("result.npy")
x1=float(input("Enter x1: "))
x2=float(input("Enter x2: "))
features=np.ndarray(shape=(6),dtype=float)
features[0]=1.0
features[1]=x1
features[2]=x2
features[3]=x1*x2
features[4]=x1**2
features[5]=x2**2
print(hypothesis(features,theta)>0.5)