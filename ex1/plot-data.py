import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
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
	for i in range(1,n):
		features[i]=(features[i]-np.mean(features[i]))/np.std(features[i])
	return features


features=load_data()
n,m=np.shape(features)
for i in range(m):
	if(features[0][i]==1):
		plt.scatter(features[1][i],features[2][i],color='blue')
	else:
		plt.scatter(features[1][i],features[2][i],color='red')
plt.xlabel("Marks in Test 1")
plt.ylabel("Marks in Test 2")
red_patch=mpatches.Patch(color='red', label='Students who failed')
bllue_patch=mpatches.Patch(color='blue',label='Students who passed')	
plt.legend(handles=[red_patch,bllue_patch])
theta=np.load("result.npy")
yp=[(theta[0]+theta[1]*0.01*t)/-theta[2] for t in range(-200,200)]
xp=[0.01*t for t in range(-200,200)]
plt.plot(xp,yp)
plt.show()