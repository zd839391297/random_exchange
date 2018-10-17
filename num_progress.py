import numpy as np

data = np.loadtxt("random.txt")
men = np.zeros(shape=(30,2))
for i in range(0,30):
    men[i][0]=i
for j in range(0,30):
    for i in range(0,30):
        a=int(data[j][i])
        men[a-1][1]+=1
print(men)



