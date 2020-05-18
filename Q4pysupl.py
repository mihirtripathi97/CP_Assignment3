


#Please read description given in Q4.c file before exicuting this file.


import numpy as np
import matplotlib.pyplot as plt


def F(K):
    y=[]
    for k in K:
        y.append(np.exp(-k*k/4)/np.sqrt(2))    #Analytical Gaussian fourier space
    return (y)

def gauss(X):
    y=[]
    for x in X:
        y.append(np.exp(-(x*x)))    #Real space gaussian
    return(y)


kc, fc = np.loadtxt("Q4rl.txt", usecols=(0, 1), unpack=True)  #kc is frequency and fc is fft



X = np.loadtxt("Q4supl.txt", usecols=(0), unpack=True)       #Getting x values
y = gauss(X)


K = np.linspace(min(kc),max(kc),1000)
Y = F(K)


plt.plot(K,Y,c='g',label = 'Analytical solution')
plt.plot(X,y,c='r',label = 'Original Function')

plt.scatter(kc,fc,c='b',label='Numerical Result using C - FFTW')

plt.xlabel("k")
plt.ylabel("~F(k)")
plt.grid(True)
plt.legend()
plt.show()

