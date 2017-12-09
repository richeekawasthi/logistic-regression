import math
import numpy as np
import sys

def sigmoid(m):
	return np.array([1.0/(1.0+math.exp(-n)) for n in m])

def load_data():
	inputs=open("./ex2data2.txt").read()
	inputl=inputs.split("\n")
	m,n=len(inputl),len(inputl[0].split(","))
	label,feature=np.ndarray(shape=(m),dtype=int),np.ndarray(shape=(m,n),dtype=float)
	for i in range(m):
		a=inputl[i].split(",")
		label[i]=int(a[-1])
		for j in range(n):
			if(j==0):
				feature[i][j]=1.0
			else:
				feature[i][j]=float(a[j-1])
	features=np.ndarray(shape=(m,6), dtype=float)
	feature=np.transpose(feature)
	features=np.transpose(features)
	features[0:3]=feature[0:3]
	features[3]=features[1]*features[2]
	features[4]=features[1]**2
	features[5]=features[2]**2
	for i in range(1,n):
		features[i]=(features[i]-np.mean(features[i]))/np.std(features[i])
	return label,np.transpose(features)

def hypothesis(features,theta):
	return sigmoid(np.dot(features,np.transpose(theta)))

def computeCost(htheta,label):
	m=np.shape(label)
	return -1.0*np.sum(label*np.log(htheta)+(1-label)*np.log(1-htheta))/m

def gradient(features,theta,label):
	htheta=hypothesis(features,theta)
	m,n=np.shape(features)
	cost=(htheta-label)/m
	return np.dot(np.transpose(features),cost)
def gradientDescent(features,theta,label,rate,iterations):
	for i in range(iterations):
		theta=theta-rate*gradient(features,theta,label)
		print("Iteration number: "+str(i+1)+" Error: "+str(computeCost(hypothesis(features,theta),label)[0]))
	return theta

label,features=load_data()
m,n=np.shape(features)
theta=np.random.randn(n)
rate=float(input("Enter Learning Rate: "))
iterations=int(input("Enter the Number of Iterations: "))
theta=gradientDescent(features,theta,label,rate,iterations)
np.save("result.npy",theta)