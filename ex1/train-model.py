import math
import numpy as np
import sys

def sigmoid(m):
	return np.array([1.0/(1.0+math.exp(-n)) for n in m])

def load_data():
	inputs=open("./ex2data1.txt").read()
	inputl=inputs.split("\n")
	m,n=len(inputl),len(inputl[0].split(","))
	label,features=np.ndarray(shape=(m),dtype=int),np.ndarray(shape=(m,n),dtype=float)
	for i in range(m):
		a=inputl[i].split(",")
		label[i]=int(a[-1])
		for j in range(n):
			if(j==0):
				features[i][j]=1.0
			else:
				features[i][j]=float(a[j-1])
	return label,features
