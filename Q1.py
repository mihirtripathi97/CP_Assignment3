#This file creates some text file and prints its results into them to use it for Q2

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return(np.sinc(X/np.pi))

def F(x):
    y=[]
    for i in x:        
        if (abs(i)<=1):
            y.append(np.sqrt(np.pi/2))
        else :
            y.append(0)
    return (y)
        
        
n=64                        #If this n is changed please change then n in Q2.c as well (It is advised to keep n an even number)
X = np.linspace(-50,50,n)

with open('Q2supl.txt', 'w') as file:
    for x in X:
        file.write("%f\n" % x)

y_a = f(X)
#print(X,f(X))

#print(y_a)

nft = np.fft.fft(y_a,norm = 'ortho')


dx = X[1]-X[0]
karr = np.fft.fftfreq(n, d = dx)
karr = 2*np.pi*karr

factor = np.exp(-1j*karr*X[0])
aft = dx*np.sqrt(n/(2.0*np.pi))*factor*nft
#print(np.real(aft))




K = np.linspace(min(karr),max(karr),1000)
Y = F(K)


with open('Q1rl.txt', 'w') as file:      # This writes the result of Q1 in a file which will be useful to compare with results of Q2
    for i in range(n):
        file.write("%f %f\n" %((karr[i]),(np.real(aft[i]))))   #First column is of K and second coloumn is of fft




plt.plot(K,Y,c='g',label = 'Analytical solution')
plt.scatter(karr,np.real(aft),c='r',label='Numerical Result')
plt.xlabel("k")
plt.ylabel("~F(k)")
plt.grid(True)
plt.legend()
plt.show()