import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
def load_data():
	inputs=open("./ex2data2.txt").read()
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
	return features
features=load_data()
n,m=np.shape(features)
for i in range(m):
	if(features[0][i]==1):
		plt.scatter(features[1][i],features[2][i],color='blue')
	else:
		plt.scatter(features[1][i],features[2][i],color='red')
plt.xlabel("Test 1")
plt.ylabel("Test 2")
red_patch=mpatches.Patch(color='red', label='Chips that failed')
bllue_patch=mpatches.Patch(color='blue',label='Chips that passed')	
plt.legend(handles=[red_patch,bllue_patch])
plt.show()