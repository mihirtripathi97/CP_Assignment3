

#Please read description given in Q3.c file before executing this file.


import numpy as np
import matplotlib.pyplot as plt


def F(x):
    y=[]
    for i in x:        
        if (abs(i)<=1):
            y.append(np.sqrt(np.pi/2))
        else :
            y.append(0)
    return (y)



kc, fc = np.loadtxt("Q3rl.txt", usecols=(0, 1), unpack=True)

K = np.linspace(min(kc),max(kc),1000)
Y = F(K)


plt.plot(K,Y,c='g',label = 'Analytical solution')

plt.scatter(kc,fc,c='b',label='Numerical Result using C - GSL')

plt.xlabel("k")
plt.ylabel("~F(k)")
plt.grid(True)
plt.legend()
plt.show()