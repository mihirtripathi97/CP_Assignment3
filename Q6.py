

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = []
    for i in x:
        y.append(5.0)
    
    return(y)


        
n=32
X = np.linspace(-50,50,n)

y_a = f(X)
#print(X,f(X))

nft = np.fft.fft(y_a,norm = 'ortho')

dx = X[1]-X[0]
karr_ = np.fft.fftfreq(n, d = dx)
karr = 2*np.pi*karr_
factor = np.exp(-1j*karr*X[0])
aft = dx*np.sqrt(n/(2.0*np.pi))*factor*nft
#print(np.real(aft))





plt.plot(X,y_a,c='g',label = 'F(x) vs x')
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Constant Function")
plt.grid()
plt.legend()
plt.show()



plt.scatter(karr,np.real(aft),c='r',label = '~F(k) vs k')
plt.xlabel("k")
plt.ylabel(" ~F(k)")
plt.title("Fourier transformed Function")
plt.grid(True)
plt.legend()
plt.show()

        







