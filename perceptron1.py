import numpy as np
import pandas as pd

x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([0,1,1,1])

w=np.random.rand(1,2)
#w=np.array([0.1,0.1])

i=1
while(i<1000):
    n=1
    index = np.random.choice(x.shape[0], n, replace=False) 
    print(index)
    if(y[index]==1 and ((np.dot(x[index],(np.transpose(w))))-1)<0):

        print("first")
        w=w+x[index]

    if(y[index]==0 and ((np.dot(x[index],(np.transpose(w))))-1)>=0):

        print("second")
        w=w-x[index]

    
    
    i=i+1	

print(w)
r=w[0][0]/w[0][1]

import matplotlib.pyplot as plt
q=[row[0] for row in x]
e=[row[1] for row in x]
f = np.linspace(0,1)
g = -(r*f)+1/w[0][1]

plt.plot(q,e, 'ro')
plt.plot(f, g, '-g')
plt.axis([0, 2, 0, 2])

plt.show()