import numpy as np
def load_data():
	inputs=open("./ex2data1.txt").read()
	inputl=inputs.split("\n")
	m,n=len(inputl),len(inputl[0].split(","))
	features=np.ndarray(shape=(n,m),dtype=float)
	for i in range(m):
		a=inputl[i].split(",")
		for j in range(n):
			if(j==0):
				features[j][i]=int(a[-1])
			else:
				features[j][i]=float(a[j-1])
	mean,std=[np.mean(features[i]) for i in range(1,n)],[np.std(features[i]) for i in range(1,n)]
	for i in range(1,n):
		features[i]=(features[i]-np.mean(features[i]))/np.std(features[i])
	return features,mean,std

def test(x,y):
	features,mean,std=load_data()
	theta=np.load("result.npy")
	test=np.array([1,(x-mean[0])/std[0],(y-mean[1]/std[1])])
	return (np.dot(np.transpose(theta),test)>0)

x=float(input("1st test: "))
y=float(input("2st test: "))
print(test(x,y))